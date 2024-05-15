"""empty message

Revision ID: d259e2b01f7b
Revises: 
Create Date: 2024-05-15 10:35:10.627986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd259e2b01f7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publication_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('video_games_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('videogame_id', sa.Integer(), nullable=True),
    sa.Column('publication_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['publication_id'], ['publication_table.id'], name=op.f('fk_review_table_publication_id_publication_table')),
    sa.ForeignKeyConstraint(['videogame_id'], ['video_games_table.id'], name=op.f('fk_review_table_videogame_id_video_games_table')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review_table')
    op.drop_table('video_games_table')
    op.drop_table('publication_table')
    # ### end Alembic commands ###