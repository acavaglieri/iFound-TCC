"""init

Revision ID: 003a21c377fb
Revises: 
Create Date: 2021-10-19 12:38:48.697968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003a21c377fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('federal_id', sa.String(length=255), nullable=False),
    sa.Column('cellphone', sa.String(length=255), nullable=False),
    sa.Column('encrypted_password', sa.String(length=255), nullable=False),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('state', sa.String(length=255), nullable=False),
    sa.Column('is_inactive', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('token', sa.String(length=255), nullable=True),
    sa.Column('is_confirmed', sa.Boolean(), nullable=False),
    sa.Column('role', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_index(op.f('ix_users_cellphone'), 'users', ['cellphone'], unique=True)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_federal_id'), 'users', ['federal_id'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_federal_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_cellphone'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
