"""adicionado campo de complemento na tabela users

Revision ID: fbd2dced187e
Revises: 74cbf559a1fc
Create Date: 2022-08-05 10:52:35.340399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbd2dced187e'
down_revision = '74cbf559a1fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('address_complement', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'address_complement')
    # ### end Alembic commands ###
