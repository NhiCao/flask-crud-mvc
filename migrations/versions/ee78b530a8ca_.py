"""empty message

Revision ID: ee78b530a8ca
Revises: 
Create Date: 2022-09-14 17:12:34.659347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee78b530a8ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    passop.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('user')
