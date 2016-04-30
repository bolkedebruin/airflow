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
    op.add_column('task_instance', sa.Column('dag_run_id',
                                             sa.Integer(),
                                             nullable=False,
                                             server_default="-1"))
    with op.batch_alter_table('task_instance') as batch_op:
        batch_op.alter_column('dag_run_id', server_default=None)


def downgrade():
    op.drop_column('task_instance', 'dag_run_id')
