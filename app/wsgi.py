"""
Point d'entrée WSGI pour Render
"""
import os
from app import app, init_db

# Configuration pour la production
if os.environ.get('DATABASE_URL'):
    # Configuration de la base de données pour Render
    database_url = os.environ.get('DATABASE_URL')
    # Render utilise postgres:// mais SQLAlchemy nécessite postgresql://
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

# Initialiser la base de données
init_db()

if __name__ == "__main__":
    app.run()