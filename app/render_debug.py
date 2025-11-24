"""
Script de debug spécifique pour Render
"""
import os
import logging
from flask import Flask
from models import db, User, Notification

# Configuration pour Render
app = Flask(__name__)
database_url = os.environ.get('DATABASE_URL', 'sqlite:///notifications.db')
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def debug_render():
    """Debug pour Render"""
    with app.app_context():
        print("=== DEBUG RENDER ===")
        print(f"DATABASE_URL: {os.environ.get('DATABASE_URL', 'Non définie')}")
        print(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        try:
            # Test connexion DB
            users = User.query.all()
            notifications = Notification.query.all()
            print(f"✓ DB OK - {len(users)} users, {len(notifications)} notifications")
            
            # Test création utilisateur si vide
            if len(users) == 0:
                print("Création d'utilisateurs de test...")
                db.create_all()
                test_user = User(name='Test User', email='test@example.com', prefers_email=True)
                db.session.add(test_user)
                db.session.commit()
                print("✓ Utilisateur de test créé")
            
            # Test notification
            from simple_notification import send_notification_direct
            if users:
                result = send_notification_direct(users[0].id, "Test Render", "Message de test")
                print(f"✓ Test notification: {result}")
            
        except Exception as e:
            print(f"✗ Erreur: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    debug_render()