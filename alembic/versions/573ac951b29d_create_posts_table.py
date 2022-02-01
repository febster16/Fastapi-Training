"""create posts table

Revision ID: 573ac951b29d
Revises: 
Create Date: 2022-02-01 23:37:08.437854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '573ac951b29d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)) 
    pass


def downgrade():
    op.drop_table('posts')
    pass

