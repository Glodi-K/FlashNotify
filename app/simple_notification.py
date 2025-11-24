"""
Version simplifiée du système de notification pour debug
"""
import logging
from models import db, User, Notification
from core.notification_system import AcademicNotifier, EmergencyType

def send_notification_direct(user_id, title, body, emergency_type="académique"):
    """Envoie une notification directement sans file d'attente"""
    try:
        # Récupération de l'utilisateur
        user = User.query.get(user_id)
        if not user:
            raise ValueError(f"Utilisateur {user_id} non trouvé")
        
        logging.info(f"Envoi direct de notification à {user.email}")
        
        # Conversion en dictionnaire
        user_dict = user.to_dict()
        
        # Détermination du type d'urgence
        emergency_enum = EmergencyType.ACADEMIC
        for et in EmergencyType:
            if et.value == emergency_type:
                emergency_enum = et
                break
        
        # Création du notifier
        notifier = AcademicNotifier()
        
        # Envoi direct
        notification_data = notifier.notify(user_dict, title, body, emergency_enum)
        
        logging.info(f"Notification envoyée avec succès à {user.email}")
        logging.info(f"Résultats: {notification_data}")
        
        return {
            "success": True,
            "notification_id": notification_data.get('notification_id'),
            "message": "Notification envoyée avec succès"
        }
        
    except Exception as e:
        logging.error(f"Erreur d'envoi de notification: {e}", exc_info=True)
        return {
            "success": False,
            "error": str(e)
        }