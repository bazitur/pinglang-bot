"""empty message

Revision ID: d1052348c356
Revises: 3e27711ebd60
Create Date: 2021-01-23 20:30:06.630664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1052348c356'
down_revision = '3e27711ebd60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reddit_post', sa.Column('timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reddit_post', 'timestamp')
    # ### end Alembic commands ###