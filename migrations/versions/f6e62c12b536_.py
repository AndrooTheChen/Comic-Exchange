"""empty message

Revision ID: f6e62c12b536
Revises: bdcd463fea60
Create Date: 2019-03-26 21:37:35.081018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6e62c12b536'
down_revision = 'bdcd463fea60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('selling', sa.Column('cgc', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('selling', 'cgc')
    # ### end Alembic commands ###
