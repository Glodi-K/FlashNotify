# ProjetPOO3 - Système de Notification Académique

Application Flask de gestion des notifications académiques avec authentification et file d'attente.

## Fonctionnalités

- 🔐 Système d'authentification avec rôles (admin/user)
- 📧 Envoi de notifications par email et SMS
- 📊 Dashboard avec statistiques
- 👥 Gestion des utilisateurs (admin)
- 🔄 File d'attente asynchrone pour les notifications
- 📱 Interface responsive

## Déploiement sur Render

### Prérequis
1. Compte GitHub
2. Compte Render (gratuit)

### Étapes de déploiement

1. **Pousser le code sur GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/votre-username/projetpoo3.git
   git push -u origin main
   ```

2. **Créer le service sur Render**
   - Aller sur [render.com](https://render.com)
   - Cliquer "New +" → "Web Service"
   - Connecter votre repository GitHub
   - Render détectera automatiquement le fichier `render.yaml`

3. **Configuration automatique**
   - Base de données PostgreSQL créée automatiquement
   - Variables d'environnement configurées
   - SSL activé automatiquement

## Variables d'environnement

- `DATABASE_URL` : URL de la base de données PostgreSQL (auto-configurée par Render)
- `SESSION_SECRET` : Clé secrète pour les sessions (générée automatiquement)

## Utilisation locale

```bash
cd app
pip install -r requirements.txt
python app.py
```

Accès : http://localhost:5000

## Comptes par défaut

- **Admin** : admin@flashnotify.local / admin123
- **User** : alice.martin@universite.edu / user123