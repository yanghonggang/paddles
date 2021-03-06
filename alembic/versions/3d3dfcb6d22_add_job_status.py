"""Add Job.status

Revision ID: 3d3dfcb6d22
Revises: 2cd0b1d5fa13
Create Date: 2013-12-05 15:45:03.026586

"""

# revision identifiers, used by Alembic.
revision = '3d3dfcb6d22'
down_revision = '2cd0b1d5fa13'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('jobs', sa.Column('status', sa.String(length=32),
                                    nullable=True))


def downgrade():
    op.drop_column('jobs', 'status')
