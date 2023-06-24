"""fixed Event.contacts

Revision ID: 23c92d3f574e
Revises: fe39345a6924
Create Date: 2021-07-14 23:25:02.473547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23c92d3f574e'
down_revision = 'fe39345a6924'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('contacts', sa.String(), nullable=True))
    op.drop_column('event', 'contacs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('contacs', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('event', 'contacts')
    # ### end Alembic commands ###