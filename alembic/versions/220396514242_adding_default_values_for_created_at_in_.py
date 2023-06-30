"""adding default values for created_at in user and liked_posts tables

Revision ID: 220396514242
Revises: a9245bf67fc7
Create Date: 2023-06-30 11:42:29.087033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '220396514242'
down_revision = 'a9245bf67fc7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(table_name='user', column_name='created_at', server_default=sa.func.now())
    op.alter_column(table_name='liked_posts', column_name='created_at', server_default=sa.func.now())


def downgrade() -> None:
    op.alter_column(table_name='user', column_name='created_at', server_default=None)
    op.alter_column(table_name='liked_posts', column_name='created_at', server_default=None)
