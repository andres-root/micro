"""Add post table

Revision ID: 76830aaea40a
Revises: 6c13535361c0
Create Date: 2020-03-03 23:31:13.285441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76830aaea40a'
down_revision = '6c13535361c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_index(op.f('ix_post_body'), 'post', ['body'], unique=True)
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_index(op.f('ix_post_body'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
