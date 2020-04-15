"""empty message

Revision ID: 1e84b608cbe7
Revises: 04109d9757eb
Create Date: 2019-03-07 04:50:10.759397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e84b608cbe7'
down_revision = '04109d9757eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('bio', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'bio')
    # ### end Alembic commands ###
