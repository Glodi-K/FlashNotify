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
    try:
        # Forcer l'initialisation si pas d'utilisateurs
        from models import User
        if User.query.count() == 0:
            logging.info("Base vide, initialisation forcée")
            from init_render_db import force_init
            force_init()
        else:
            init_db()
        
        init_queues()
        logging.info("Initialisation réussie")
    except Exception as e:
        logging.error(f"Erreur d'initialisation: {e}", exc_info=True)

if __name__ == "__main__":
    app.run()