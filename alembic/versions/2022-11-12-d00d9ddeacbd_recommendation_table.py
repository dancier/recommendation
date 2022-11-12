"""recommendation-table

Revision ID: d00d9ddeacbd
Revises: 4263c33fcff8
Create Date: 2022-11-12 08:50:17.976417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd00d9ddeacbd'
down_revision = '4263c33fcff8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    DROP TABLE IF EXISTS recommendations;
    CREATE TABLE IF NOT EXISTS recommendations
    (
        dancer_a_id uuid NOT NULL,
        dancer_a_version integer NOT NULL,
        dancer_b_id uuid NOT NULL,
        dancer_b_version integer NOT NULL,
        created timestamp without time zone,
        score smallint
    )
    """)


def downgrade() -> None:
    op.execute("""
        drop table if exists recommendations
    """)
