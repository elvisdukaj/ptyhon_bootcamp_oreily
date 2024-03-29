"""username cannot be nullable

Revision ID: 8fd8e29dcdf6
Revises: e039f3143aa3
Create Date: 2023-06-30 11:48:51.447581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fd8e29dcdf6'
down_revision = 'e039f3143aa3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=25),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=25),
               nullable=True)
    # ### end Alembic commands ###
