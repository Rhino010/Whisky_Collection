"""empty message

Revision ID: 26e276e637ea
Revises: 
Create Date: 2024-07-04 14:58:34.164411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26e276e637ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('whisky',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('brand', sa.String(length=150), nullable=False),
    sa.Column('country_state', sa.String(length=150), nullable=False),
    sa.Column('batch', sa.String(length=150), nullable=True),
    sa.Column('proof', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('whisky')
    op.drop_table('user')
    # ### end Alembic commands ###