"""empty message

Revision ID: 3209e7593a1c
Revises: adf4c295a5e8
Create Date: 2023-04-20 22:20:06.356511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3209e7593a1c'
down_revision = 'adf4c295a5e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pending_friendship',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pending_friend_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pending_friend_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'pending_friend_id')
    )
    op.drop_table('pending__friendship')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pending__friendship',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('pending_friend_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['pending_friend_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pending_friendship')
    # ### end Alembic commands ###
