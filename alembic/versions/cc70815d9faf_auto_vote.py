"""auto-vote

Revision ID: cc70815d9faf
Revises: dbd759c2ef1a
Create Date: 2022-02-01 23:44:33.412297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc70815d9faf'
down_revision = 'dbd759c2ef1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vote',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vote')
    # ### end Alembic commands ###
