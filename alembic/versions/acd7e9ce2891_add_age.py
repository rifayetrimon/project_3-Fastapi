"""add age

Revision ID: acd7e9ce2891
Revises: 
Create Date: 2024-10-16 11:40:17.899616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'acd7e9ce2891'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass
    # op.add_column('users', sa.Column('age', sa.Integer()))


def downgrade() -> None:
    pass
    # op.drop_column('users', 'age')
