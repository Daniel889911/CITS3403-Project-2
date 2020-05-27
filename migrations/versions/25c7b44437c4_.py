"""empty message

Revision ID: 25c7b44437c4
Revises: 
Create Date: 2020-05-27 23:23:02.021586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25c7b44437c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('qanswers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quiz_name', sa.String(length=64), nullable=True),
    sa.Column('submit_name', sa.String(length=64), nullable=True),
    sa.Column('a1', sa.String(length=256), nullable=True),
    sa.Column('a2', sa.String(length=256), nullable=True),
    sa.Column('a3', sa.String(length=256), nullable=True),
    sa.Column('q1copy', sa.String(length=256), nullable=True),
    sa.Column('q2copy', sa.String(length=256), nullable=True),
    sa.Column('q3copy', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_table('quiz',
    sa.Column('quizname', sa.String(length=64), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('q1', sa.String(length=256), nullable=True),
    sa.Column('q2', sa.String(length=256), nullable=True),
    sa.Column('q3', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('quizname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quiz')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('qanswers')
    # ### end Alembic commands ###
