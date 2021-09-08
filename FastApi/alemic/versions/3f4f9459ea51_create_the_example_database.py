"""Create the example Database

Revision ID: 3f4f9459ea51
Revises: 
Create Date: 2021-07-05 22:53:53.029451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f4f9459ea51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'blogs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('author',sa.String(50)),
        sa.Column('body',sa.String(50)),
        sa.Column('publishedStatus',sa.String(50)),
        sa.Column('test',sa.String(50))
    )

def downgrade():
    op.drop_table('blogs')
