"""Add a column

Revision ID: b4d4a12ebce6
Revises: fe50726a1371
Create Date: 2021-07-06 11:26:55.245470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4d4a12ebce6'
down_revision = 'fe50726a1371'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('blogs', sa.Column('test4', sa.String(50)))
       

def downgrade():
    op.drop_table('blogs')
