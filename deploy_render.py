"""
Script de déploiement pour Render
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} réussi")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} échoué")
        print(f"Erreur: {e.stderr}")
        return False

def main():
    """Fonction principale de déploiement"""
    print("🚀 DÉPLOIEMENT PROJETPOO3 SUR RENDER")
    print("=" * 50)
    
    # Vérifier que nous sommes dans le bon répertoire
    if not os.path.exists("render.yaml"):
        print("❌ Fichier render.yaml non trouvé. Assurez-vous d'être dans le répertoire racine du projet.")
        sys.exit(1)
    
    # Étapes de déploiement
    steps = [
        ("git add .", "Ajout des fichiers au git"),
        ("git commit -m \"Fix: Correction du système de notification pour Render\"", "Commit des modifications"),
        ("git push origin main", "Push vers le repository"),
    ]
    
    success = True
    for command, description in steps:
        if not run_command(command, description):
            success = False
            break
    
    if success:
        print("\n🎉 Déploiement terminé avec succès!")
        print("📋 Prochaines étapes:")
        print("1. Vérifiez les logs de déploiement sur Render")
        print("2. Testez l'application une fois déployée")
        print("3. Vérifiez que les notifications fonctionnent")
    else:
        print("\n❌ Déploiement échoué. Vérifiez les erreurs ci-dessus.")

if __name__ == "__main__":
    main()