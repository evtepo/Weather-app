"""Role changes

Revision ID: 47ac353fe855
Revises: f83e01c17001
Create Date: 2023-09-17 17:50:55.655130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47ac353fe855'
down_revision: Union[str, None] = 'f83e01c17001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'permissions')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('permissions', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
