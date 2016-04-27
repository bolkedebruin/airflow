"""change uniqueconstraint for dagrun

Revision ID: 88537a2fcad
Revises: 182c0d1598ee
Create Date: 2016-04-27 23:21:26.574027

"""

# revision identifiers, used by Alembic.
revision = '88537a2fcad'
down_revision = '182c0d1598ee'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_constraint("dag_id", "dag_run", "unique")
    op.create_unique_constraint("dag_id", "dag_run", ["dag_id", "execution_date", "run_id"])


def downgrade():
    op.drop_constraint("dag_id", "dag_run", "unique")
    op.create_unique_constraint("dag_id", "dag_run", ["dag_id", "execution_date"])
