"""
Configuration pour l'application Flask
"""
import os

class Config:
    """Configuration de base"""
    SECRET_KEY = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuration de la base de données
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///notifications.db')
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = DATABASE_URL

class DevelopmentConfig(Config):
    """Configuration de développement"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///notifications.db'

class ProductionConfig(Config):
    """Configuration de production"""
    DEBUG = False
    # Utilise la variable d'environnement DATABASE_URL de Render

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}