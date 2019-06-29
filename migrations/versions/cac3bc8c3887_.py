"""empty message

Revision ID: cac3bc8c3887
Revises: bb59c3a61758
Create Date: 2019-06-28 04:39:11.832523

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cac3bc8c3887'
down_revision = 'bb59c3a61758'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_is_deleted', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(collation='utf8mb4_general_ci', length=24), nullable=True),
    sa.Column('email', mysql.VARCHAR(collation='utf8mb4_general_ci', length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('password', mysql.VARCHAR(collation='utf8mb4_general_ci', length=128), server_default=sa.text("''"), nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('deleted_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('is_deleted', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('updated_at', mysql.TIMESTAMP(), nullable=True),
    sa.CheckConstraint('(`is_deleted` in (0,1))', name='users_chk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=True)
    op.create_index('ix_users_is_deleted', 'users', ['is_deleted'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    # ### end Alembic commands ###
