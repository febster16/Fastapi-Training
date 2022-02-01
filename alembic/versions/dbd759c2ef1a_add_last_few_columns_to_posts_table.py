"""add last few columns to posts table

Revision ID: dbd759c2ef1a
Revises: 9462ac571609
Create Date: 2022-02-01 23:43:39.534147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbd759c2ef1a'
down_revision = '9462ac571609'
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
