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
    op.get_bind().execute("""
    -- Table: public.eventlog

    -- DROP TABLE IF EXISTS public.eventlog;
    
    CREATE TABLE IF NOT EXISTS public.eventlog
    (
        id uuid NOT NULL,
        topic character varying(256) COLLATE pg_catalog."default",
        meta_data jsonb,
        payload jsonb,
        created timestamp without time zone,
        user_id uuid,
        roles text[] COLLATE pg_catalog."default",
        CONSTRAINT eventlog_pkey PRIMARY KEY (id)
    )
    
    TABLESPACE pg_default;
    
    ALTER TABLE IF EXISTS public.eventlog
        OWNER to recommendation;
    """)
    pass


def downgrade() -> None:
    op.drop_table("eventlog")
    pass
