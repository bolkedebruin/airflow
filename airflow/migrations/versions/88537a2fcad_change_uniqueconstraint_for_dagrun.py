# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
from alembic import context
import sqlalchemy as sa


def upgrade():
    url = context.config.get_main_option("sqlalchemy.url")
    if url.find("postgresql") > -1:
        op.drop_constraint("dag_run_dag_id_execution_date_key", "dag_run")
        op.create_unique_constraint("uq_dag_run_dag_id_execution_date_run_id",
                                    "dag_run", ["dag_id", "execution_date", "run_id"])
    elif url.find("mysql") > -1:
        op.drop_constraint("dag_id", "dag_run", "unique")
        op.create_unique_constraint("uq_dag_run_dag_id_execution_date_run_id",
                                    "dag_run", ["dag_id", "execution_date", "run_id"])
    elif url.find("sqlite") > -1:
        naming_convention = {
            "fk":
                "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s_%(column_1_name)s",
        }
        with op.batch_alter_table('dag_run',
                                  naming_convention=naming_convention,
                                  ) as batch_op:
            batch_op.drop_constraint("uq_dag_run_dag_id_execution_date", type_="unique")
            batch_op.create_unique_constraint("uq_dag_run_dag_id_execution_date_run_id",
                                              ["dag_id", "execution_date", "run_id"])


def downgrade():
    url = context.config.get_main_option("sqlalchemy.url")
    if url.find("sqlite") > -1:
        with op.batch_alter_table('dag_run', table_args=(
                sa.UniqueConstraint('dag_id',
                                    'run_id',
                                    name="uq_dag_run_dag_id_run_id"),
        )) as batch_op:
            batch_op.create_unique_constraint("uq_dag_run_dag_id_run_id",
                                              ["dag_id", "execution_date"])

    else:
        op.drop_constraint("uq_dag_run_dag_id_execution_date_run_id",
                           "dag_run", "unique")
        # None is used to get the automated naming scheme from the db
        op.create_unique_constraint(None, "dag_run", ["dag_id", "execution_date"])
