"""add foreign key to posts table

Revision ID: 9462ac571609
Revises: b07a2c154051
Create Date: 2022-02-01 23:42:45.233106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9462ac571609'
down_revision = 'b07a2c154051'
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
