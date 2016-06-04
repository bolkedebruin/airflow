"""Add TaskInstanceCounters

Revision ID: 060e1cc0d547
Revises: babb253b528e
Create Date: 2016-06-04 23:00:21.166928

"""

# revision identifiers, used by Alembic.
revision = '060e1cc0d547'
down_revision = '2e82aab8ef20'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'task_counter',
        sa.Column('task_id', sa.String(length=250), nullable=False),
        sa.Column('dag_id', sa.String(length=250), nullable=False),
        sa.Column('execution_date', sa.DateTime(), nullable=False),
        sa.Column('state', sa.String(length=50), nullable=False),
        sa.Column('counter', sa.Integer, nullable=False, default=0),
        sa.PrimaryKeyConstraint('task_id', 'dag_id', 'execution_date', 'state')
    )


def downgrade():
    op.drop_table('task_counter')
