"""
Script pour forcer l'initialisation de la DB sur Render
"""
import os
from app import app, init_db
from models import db, User
from core.auth import auth_manager

def force_init():
    """Force l'initialisation de la DB"""
    with app.app_context():
        print("=== INITIALISATION FORCÉE DB RENDER ===")
        
        # Supprimer et recréer les tables
        db.drop_all()
        db.create_all()
        print("✓ Tables recréées")
        
        # Créer utilisateurs
        admin = User(name='Admin', email='admin@flashnotify.local', role='admin', prefers_email=True)
        admin._password = auth_manager.hash_password('admin123')
        
        user1 = User(name='Alice Martin', email='alice@test.com', role='user', prefers_email=True)
        user1._password = auth_manager.hash_password('user123')
        
        user2 = User(name='Bob Dupont', email='bob@test.com', role='user', prefers_email=False)
        user2._password = auth_manager.hash_password('user123')
        
        db.session.add_all([admin, user1, user2])
        db.session.commit()
        print("✓ Utilisateurs créés")
        
        # Vérifier
        count = User.query.count()
        print(f"✓ {count} utilisateurs en base")

if __name__ == "__main__":
    force_init()