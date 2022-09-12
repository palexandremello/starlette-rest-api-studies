"""spreadsheet

Revision ID: adc443570c81
Revises: cf5d337f90b6
Create Date: 2022-09-12 02:13:19.505909

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text, ForeignKey


# revision identifiers, used by Alembic.
revision = 'adc443570c81'
down_revision = 'cf5d337f90b6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'spreadsheet',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('initial_date', sa.DateTime, nullable=False),
        sa.Column('final_date', sa.DateTime, nullable=False),
        sa.Column('filename', sa.String(100), nullable=False),
        sa.Column('link', sa.Text, nullable=True),
        sa.Column('path', sa.Text, nullable=True),
        sa.Column('status_id', sa.Integer, ForeignKey('status.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=text('now()'), nullable=False)

    )



def downgrade() -> None:
    op.drop_table('spreadsheet')
