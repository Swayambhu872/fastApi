"""alter a column

Revision ID: 8de9fcc1ff46
Revises: 2e3227884e3e
Create Date: 2021-07-07 11:25:07.053333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8de9fcc1ff46'
down_revision = '2e3227884e3e'
branch_labels = None
depends_on = None


def upgrade():
     op.create_check_constraint('create_check_constraint',"blogs","test3 in ('second', 'first')")
       

def downgrade():
    op.drop_table('blogs')
