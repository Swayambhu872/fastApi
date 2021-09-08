"""Add a column

Revision ID: fe50726a1371
Revises: 876d388c181d
Create Date: 2021-07-06 11:15:26.265404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe50726a1371'
down_revision = '876d388c181d'
branch_labels = None
depends_on = None


def upgrade():
   op.add_column('blogs', sa.Column('test5', sa.String(50)))
       

def downgrade():
    op.drop_table('blogs')
