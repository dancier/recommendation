"""location view

Revision ID: 4b74efae83c5
Revises: dbad21cb4ed7
Create Date: 2022-11-10 20:18:17.623939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b74efae83c5'
down_revision = 'dbad21cb4ed7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
DROP MATERIALIZED VIEW IF EXISTS dancers;
CREATE MATERIALIZED VIEW dancers AS 
	WITH max_version_per_dancer AS
	(SELECT (payload ->> 'id')::uuid AS dancer_id,
			MAX((payload ->> 'version')::integer) AS "version"
		FROM eventlog
		WHERE topic = 'profile-updated'
		GROUP BY (payload ->> 'id')
	)
	SELECT dancer_id,
		   (PAYLOAD ->> 'longitude')::float AS longitude,
	       (PAYLOAD ->> 'latitude')::float AS LATITUDE,
	       payload as payload,
	       max_version_per_dancer."version" AS "version"
 FROM max_version_per_dancer
 JOIN eventlog 
   ON max_version_per_dancer.dancer_id = (eventlog.payload->>'id')::uuid
  AND max_version_per_dancer."version" = (payload->>'version')::integer;
    """)


def downgrade() -> None:
    op.execute("""DROP MATERIALIZED VIEW IF EXISTS dancers""")