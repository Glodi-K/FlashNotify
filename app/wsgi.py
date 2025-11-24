"""
Point d'entrée WSGI pour Render
"""
import os
import logging
from app import app, init_db
from core.queue import init_queues

# Configuration des logs pour la production
logging.basicConfig(level=logging.INFO)

# Configuration pour la production
if os.environ.get('DATABASE_URL'):
    # Configuration de la base de données pour Render
    database_url = os.environ.get('DATABASE_URL')
    # Render utilise postgres:// mais SQLAlchemy nécessite postgresql://
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

# Initialiser la base de données et les files d'attente
with app.app_context():
    init_db()
    init_queues()

if __name__ == "__main__":
    app.run()