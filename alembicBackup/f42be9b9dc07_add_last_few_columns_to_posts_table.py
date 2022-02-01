"""add last few columns to posts table

Revision ID: f42be9b9dc07
Revises: 1c48ace08567
Create Date: 2022-02-01 00:38:27.746809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f42be9b9dc07'
down_revision = '1c48ace08567'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', 
                sa.Column('published', sa.Boolean, nullable=False, server_default='TRUE'))
    op.add_column('posts', 
                sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
