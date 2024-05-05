"""initial migration

Revision ID: 208a4d4c3df8
Revises: 817e052b427f
Create Date: 2024-05-05 04:32:09.791397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '208a4d4c3df8'
down_revision: Union[str, None] = '817e052b427f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('created_by', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'events', 'users', ['created_by'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'created_by')
    # ### end Alembic commands ###
