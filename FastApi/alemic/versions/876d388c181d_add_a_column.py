"""Add a column

Revision ID: 876d388c181d
Revises: 06b6e071258c
Create Date: 2021-07-06 10:59:23.634839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '876d388c181d'
down_revision = '06b6e071258c'
branch_labels = None
depends_on = None


def upgrade():
     op.add_column('blogs', sa.Column('test2', sa.String(50)))

def downgrade():
    op.drop_table('blogs')
