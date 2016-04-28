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
