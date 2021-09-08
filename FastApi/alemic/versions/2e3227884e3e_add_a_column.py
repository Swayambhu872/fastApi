"""Add a column

Revision ID: 2e3227884e3e
Revises: 39cf5321afa4
Create Date: 2021-07-06 11:43:47.835024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e3227884e3e'
down_revision = '39cf5321afa4'
branch_labels = None
depends_on = None


def upgrade():
     op.add_column('blogs', sa.Column('test7', sa.String(50)))
       

def downgrade():
    op.drop_table('blogs')
