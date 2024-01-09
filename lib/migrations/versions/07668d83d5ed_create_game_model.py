"""Create Game Model

Revision ID: 07668d83d5ed
Revises: 55bae6207fef
Create Date: 2024-01-09 02:39:59.953526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07668d83d5ed'
down_revision = '55bae6207fef'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('platform', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    # ### end Alembic commands ###
