"""Add a column

Revision ID: 5d2a6e461ace
Revises: 3f4f9459ea51
Create Date: 2021-07-05 23:06:31.034137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d2a6e461ace'
down_revision = '3f4f9459ea51'
branch_labels = None
depends_on = None


def upgrade():
   op.add_column('blogs', sa.Column('last_transaction_date', sa.DateTime))
       

def downgrade():
    op.drop_table('blogs')
