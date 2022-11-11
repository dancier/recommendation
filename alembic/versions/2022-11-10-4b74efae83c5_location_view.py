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
DROP MATERIALIZED VIEW IF EXISTS dancer_locations;
CREATE MATERIALIZED VIEW DANCER_LOCATIONS AS WITH MAX_VERSION_PER_DANCER AS
	(SELECT (PAYLOAD ->> 'id') AS DANCER_ID,
			MAX((PAYLOAD ->> 'version')::integer) AS "version"
		FROM EVENTLOG
		WHERE TOPIC = 'profile-updated'
		GROUP BY (PAYLOAD ->> 'id')
	) 
	SELECT DANCER_ID::uuid,
	(PAYLOAD ->> 'longitude')::float AS LONGITUDE,
	(PAYLOAD ->> 'latitude')::float AS LATITUDE
FROM MAX_VERSION_PER_DANCER
JOIN EVENTLOG 
  ON MAX_VERSION_PER_DANCER.DANCER_ID = EVENTLOG.PAYLOAD ->> 'id' 
  and MAX_VERSION_PER_DANCER."version" = (PAYLOAD ->> 'version')::integer;
    """)


def downgrade() -> None:
    op.execute("""DROP MATERIALIZED VIEW IF EXISTS dancer_locations""")