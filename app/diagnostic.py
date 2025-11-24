"""
Script de diagnostic pour vérifier le système de notification
"""
import os
import logging
from app import app, init_db
from models import db, User, Notification
from core.queue import thread_pool_queue, async_queue
from core.notification_system import AcademicNotifier, EmergencyType

logging.basicConfig(level=logging.INFO)

def test_database():
    """Test de la connexion à la base de données"""
    try:
        with app.app_context():
            users = User.query.all()
            notifications = Notification.query.all()
            print(f"✓ Base de données OK - {len(users)} utilisateurs, {len(notifications)} notifications")
            return True
    except Exception as e:
        print(f"✗ Erreur base de données: {e}")
        return False

def test_notification_system():
    """Test du système de notification"""
    try:
        notifier = AcademicNotifier()
        user_dict = {
            'id': 1,
            'email': 'test@example.com',
            'phone': '+33123456789',
            'prefers_email': True
        }
        
        with app.app_context():
            result = notifier.notify(user_dict, "Test", "Message de test", EmergencyType.ACADEMIC)
            print(f"✓ Système de notification OK - {len(result.get('results', []))} canaux utilisés")
            return True
    except Exception as e:
        print(f"✗ Erreur système de notification: {e}")
        return False

def test_queue_system():
    """Test du système de files d'attente"""
    try:
        # Test ThreadPool
        if thread_pool_queue.running:
            print("✓ File d'attente ThreadPool active")
        else:
            print("✗ File d'attente ThreadPool inactive")
        
        # Test AsyncQueue (seulement en développement)
        if not os.environ.get('DATABASE_URL'):
            if async_queue.running:
                print("✓ File d'attente asynchrone active")
            else:
                print("✗ File d'attente asynchrone inactive")
        else:
            print("ℹ File d'attente asynchrone désactivée en production")
        
        return True
    except Exception as e:
        print(f"✗ Erreur système de files d'attente: {e}")
        return False

def main():
    """Fonction principale de diagnostic"""
    print("=== DIAGNOSTIC DU SYSTÈME DE NOTIFICATION ===")
    print(f"Environnement: {'Production' if os.environ.get('DATABASE_URL') else 'Développement'}")
    print()
    
    # Initialisation
    with app.app_context():
        init_db()
    
    # Tests
    db_ok = test_database()
    notif_ok = test_notification_system()
    queue_ok = test_queue_system()
    
    print()
    if all([db_ok, notif_ok, queue_ok]):
        print("✓ Tous les tests sont passés avec succès!")
    else:
        print("✗ Certains tests ont échoué. Vérifiez les logs ci-dessus.")

if __name__ == "__main__":
    main()