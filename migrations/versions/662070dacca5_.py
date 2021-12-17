"""empty message

Revision ID: 662070dacca5
Revises: 80256db5b83c
Create Date: 2021-12-16 22:04:38.436207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '662070dacca5'
down_revision = '80256db5b83c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('placa', sa.String(length=64), nullable=True),
    sa.Column('modelo', sa.String(length=64), nullable=True),
    sa.Column('fabricante', sa.String(length=64), nullable=True),
    sa.Column('renavan', sa.String(length=64), nullable=True),
    sa.Column('combustivel', sa.String(length=64), nullable=True),
    sa.Column('lotacao', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('placa'),
    sa.UniqueConstraint('renavan')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    # ### end Alembic commands ###
