"""Add a column

Revision ID: 06b6e071258c
Revises: 5d2a6e461ace
Create Date: 2021-07-05 23:19:49.976905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06b6e071258c'
down_revision = '5d2a6e461ace'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('blogs', sa.Column('pointer', sa.String(50)))
       

def downgrade():
    op.drop_table('blogs')
