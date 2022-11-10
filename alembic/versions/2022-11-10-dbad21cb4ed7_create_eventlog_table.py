"""create eventlog table

Revision ID: dbad21cb4ed7
Revises: 
Create Date: 2022-11-10 18:09:37.586226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbad21cb4ed7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("foo")
    pass


def downgrade() -> None:
    op.drop_table("foo")
    pass
