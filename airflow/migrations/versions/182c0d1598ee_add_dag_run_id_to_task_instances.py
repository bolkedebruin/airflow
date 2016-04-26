"""Add dag_run_id to task instances

Revision ID: 182c0d1598ee
Revises: 15513af28935
Create Date: 2016-04-26 23:58:30.899895

"""

# revision identifiers, used by Alembic.
revision = '182c0d1598ee'
down_revision = '15513af28935'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('task_instance', sa.Column('dag_run_id', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('task_instance', 'dag_run_id')
