"""insert pair

Revision ID: 1789cc7556db
Revises: 4b74efae83c5
Create Date: 2022-11-10 22:46:10.992818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1789cc7556db'
down_revision = '4b74efae83c5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""

CREATE OR REPLACE FUNCTION array_uniq_sort(anyarray) 
RETURNS anyarray 
AS $$
SELECT array_agg(DISTINCT f ORDER BY f) FROM unnest($1) f;
$$ LANGUAGE sql IMMUTABLE;

create table pairs (
  pair  uuid[],
CONSTRAINT unique_pairs UNIQUE (pair)
);

create or replace function insert_pair(a_dancer_id uuid, b_dancer_id uuid)
returns void
language plpgsql
as $$
declare
  
begin
  insert into pairs values(
  array_uniq_sort(ARRAY[a_dancer_id, b_dancer_id])
) on conflict do nothing;

end;
$$

    """)


def downgrade() -> None:
    op.drop_table("pairs")
    op.execute("""
        drop FUNCTION if exists array_uniq_sort(anyarray);
        drop FUNCTION if exists insert_pair(a_dancer_id uuid, b_dancer_id uuid);
    """)
