"""add content column

Revision ID: 079f6551268d
Revises: 573ac951b29d
Create Date: 2022-02-01 23:40:15.934210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '079f6551268d'
down_revision = '573ac951b29d'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_column('posts', 'content')
    pass

