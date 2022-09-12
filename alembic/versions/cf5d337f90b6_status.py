
"""status

Revision ID: cf5d337f90b6
Revises: 
Create Date: 2022-09-12 01:43:18.519924

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

from app.infra.repos.config.database_config import DatabaseConnectionHandler

# revision identifiers, used by Alembic.
revision = 'cf5d337f90b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'status',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=text('now()'), nullable=False)

    )
    seed()


def seed() -> None:
    db_connection_handler = DatabaseConnectionHandler()
    engine = db_connection_handler.get_engine()
    engine.execute(
        '''  
             INSERT INTO status (name)
             VALUES
             ('Novo'),
             ('Em Andamento'),
             ('Concluído'),
             ('Erro')

           
        '''
    )

def downgrade() -> None:
    db_connection_handler = DatabaseConnectionHandler()
    engine = db_connection_handler.get_engine()
    engine.execute(
        '''  
             DELETE from status
             WHERE name in ('Novo', 'Em Andamento', 'Concluído', 'Erro');
        '''
    )
    op.drop_table('status')
