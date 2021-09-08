"""Add a column

Revision ID: 8ee4d73ce740
Revises: b4d4a12ebce6
Create Date: 2021-07-06 11:28:02.558556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ee4d73ce740'
down_revision = 'b4d4a12ebce6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('blogs', sa.Column('test5', sa.String(50)))
       

def downgrade():
    op.drop_table('blogs')
