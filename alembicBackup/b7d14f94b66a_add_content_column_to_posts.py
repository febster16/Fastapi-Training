"""add content column to posts

Revision ID: b7d14f94b66a
Revises: cc3ab7183022
Create Date: 2022-01-31 14:59:19.582984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7d14f94b66a'
down_revision = 'cc3ab7183022'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_column('posts', 'content')
    pass
