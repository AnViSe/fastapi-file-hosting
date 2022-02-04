"""mixin

Revision ID: 2e29fee4851b
Revises: 8546557970c4
Create Date: 2022-02-04 04:55:48.190362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e29fee4851b'
down_revision = '8546557970c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('files', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('files', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('files', 'updated_at')
    op.drop_column('files', 'created_at')
    # ### end Alembic commands ###