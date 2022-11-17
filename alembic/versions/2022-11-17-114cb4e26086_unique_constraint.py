"""unique-constraint

Revision ID: 114cb4e26086
Revises: d00d9ddeacbd
Create Date: 2022-11-17 10:30:22.288862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '114cb4e26086'
down_revision = 'd00d9ddeacbd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    create unique index on_recommendaton_per_pair on recommendations (
	dancer_a_id,
	dancer_b_id
    );
    """)
    op.execute("""
    alter table recommendations 
      add constraint unique_recommendation_per_per
	  UNIQUE using index on_recommendaton_per_pair;
    """)


def downgrade() -> None:
    op.execute("""alter table recommendations
    drop constraint unique_recommendation_per_per;
    """)
