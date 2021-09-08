"""Add a column

Revision ID: 39cf5321afa4
Revises: 8ee4d73ce740
Create Date: 2021-07-06 11:29:19.568987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39cf5321afa4'
down_revision = '8ee4d73ce740'
branch_labels = None
depends_on = None


def upgrade():
     op.add_column('blogs', sa.Column('test6', sa.String(50)))
       

def downgrade():
    op.drop_table('blogs')
