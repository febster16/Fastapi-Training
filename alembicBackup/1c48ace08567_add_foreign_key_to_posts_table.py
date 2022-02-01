"""add foreign key to posts table

Revision ID: 1c48ace08567
Revises: eb6b35e581ab
Create Date: 2022-01-31 15:13:49.373614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c48ace08567'
down_revision = 'eb6b35e581ab'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                  sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', 
                          local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE')
    pass

def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'user_id')
    pass
