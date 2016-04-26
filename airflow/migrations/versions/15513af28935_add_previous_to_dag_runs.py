"""Add previous to dag runs

Revision ID: 15513af28935
Revises: 2e82aab8ef20
Create Date: 2016-04-26 20:43:22.778551

"""

# revision identifiers, used by Alembic.
revision = '15513af28935'
down_revision = '2e82aab8ef20'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('dag_run', sa.Column('previous', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('dag_run', 'previous')
