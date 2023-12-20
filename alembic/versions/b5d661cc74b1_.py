"""empty message

Revision ID: b5d661cc74b1
Revises: 
Create Date: 2023-12-19 18:53:49.584463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5d661cc74b1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genders',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=32), nullable=False),
    sa.Column('slug', sa.VARCHAR(length=32), nullable=False),
    sa.CheckConstraint("slug not like '%%%%' "),
    sa.CheckConstraint('length(name) >= 2'),
    sa.CheckConstraint('length(slug) >= 2'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('accounts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=128), nullable=False),
    sa.Column('body', sa.VARCHAR(length=250), nullable=False),
    sa.Column('age', sa.DECIMAL(precision=3, scale=0), nullable=False),
    sa.Column('gender_id', sa.SMALLINT(), nullable=False),
    sa.Column('date_created', sa.TIMESTAMP(), nullable=False),
    sa.Column('is_published', sa.BOOLEAN(), nullable=True),
    sa.Column('slug', sa.VARCHAR(length=128), nullable=True),
    sa.CheckConstraint('age > 18'),
    sa.CheckConstraint('length(body) >=50'),
    sa.CheckConstraint('length(title) >=2'),
    sa.ForeignKeyConstraint(['gender_id'], ['genders.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accounts')
    op.drop_table('genders')
    # ### end Alembic commands ###