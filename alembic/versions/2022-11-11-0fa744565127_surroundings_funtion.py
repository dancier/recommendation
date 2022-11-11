"""surroundings funtion

Revision ID: 0fa744565127
Revises: 1789cc7556db
Create Date: 2022-11-11 10:42:38.574445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fa744565127'
down_revision = '1789cc7556db'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    drop function if exists surroundings(uuid);
CREATE OR REPLACE FUNCTION surroundings(
	dancer_id_ uuid
)  
returns table (
	dancer_id uuid
) 
AS
$BODY$
  DECLARE
	dancer record;
	lat_min float;
	lat_max float;
	long_min float;
	long_max float;
  BEGIN
    select * from dancers into dancer where dancers.dancer_id = dancer_id_ limit 1;
	lat_min := dancer.latitude - 0.8;
	lat_max := dancer.latitude + 0.8;
	long_min := dancer.longitude - 0.8;
	long_max := dancer.longitude + 0.8;
	return query
		select dancers.dancer_id 
		  from dancers
		 where dancers.longitude BETWEEN long_min AND long_max
		   and dancers.latitude  BETWEEN lat_min AND lat_max;
  END;
$BODY$ LANGUAGE plpgsql;
    """)


def downgrade() -> None:
    op.execute("""
    drop function surroundings(uuid);
    """)

