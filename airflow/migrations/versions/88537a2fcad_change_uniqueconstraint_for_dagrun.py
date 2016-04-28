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
import sqlalchemy as sa


def upgrade():
    op.drop_constraint("dag_id", "dag_run", "unique")
    op.create_unique_constraint("dag_id", "dag_run", ["dag_id", "execution_date", "run_id"])


def downgrade():
    op.drop_constraint("dag_id", "dag_run", "unique")
    op.create_unique_constraint("dag_id", "dag_run", ["dag_id", "execution_date"])
