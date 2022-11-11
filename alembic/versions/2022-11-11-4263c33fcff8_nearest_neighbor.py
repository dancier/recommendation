"""nearest neighbor

Revision ID: 4263c33fcff8
Revises: 0fa744565127
Create Date: 2022-11-11 12:47:52.466844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4263c33fcff8'
down_revision = '0fa744565127'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
drop function if exists nearest_neighbors();
create or replace function nearest_neighbors()
   returns void
   language plpgsql
  as
$$
declare 
	any_dancer record;
	near_dancer record;
	counter integer := 0;
begin
   truncate pairs;
   for any_dancer in select *
          from dancer_locations
   loop
   		counter := counter + 1;
		for near_dancer in select * from surroundings(any_dancer.dancer_id)
			loop
				perform insert_pair(any_dancer.dancer_id, near_dancer.dancer_id);
			end loop;
   end loop;
end;
$$;
    """)


def downgrade() -> None:
    op.execute("""drop function  nearest_neighbors()""")
