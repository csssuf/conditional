"""Add Date to Submitted Major Projects

Revision ID: 6ae578b76143
Revises: 5615d58892a1
Create Date: 2017-05-21 22:59:23.917438

"""

# revision identifiers, used by Alembic.
revision = '6ae578b76143'
down_revision = '5615d58892a1'

from alembic import op
from datetime import datetime
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('major_projects', sa.Column('date', sa.Date(), server_default=datetime.now().strftime("%Y-%m-%d"), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('major_projects', 'date')
    ### end Alembic commands ###
