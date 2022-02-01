"""create posts table

Revision ID: cc3ab7183022
Revises: 
Create Date: 2022-01-31 14:48:28.556215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc3ab7183022'
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
