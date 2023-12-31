"""empty message

Revision ID: 334de8709b47
Revises: 175802ef6cdf
Create Date: 2023-04-12 19:31:51.203117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '334de8709b47'
down_revision = '175802ef6cdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_upcoming', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('is_upcoming')

    # ### end Alembic commands ###
