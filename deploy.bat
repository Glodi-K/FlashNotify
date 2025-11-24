@echo off
REM Script de deploiement FlashNotify POO3 pour Windows
echo === Deploiement FlashNotify POO3 ===

REM Verification de Docker
echo Verification de Docker...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Erreur: Docker n est pas installe ou ne fonctionne pas
    pause
    exit /b 1
)

docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Erreur: Docker Compose n est pas installe
    pause
    exit /b 1
)

echo Docker OK

REM Construction de l image
echo Construction de l image Docker...
docker-compose build
if %errorlevel% neq 0 (
    echo Erreur lors de la construction
    pause
    exit /b 1
)

REM Demarrage des services
echo Demarrage des services...
docker-compose up -d
if %errorlevel% neq 0 (
    echo Erreur lors du demarrage
    pause
    exit /b 1
)

REM Attente du demarrage
echo Attente du demarrage complet...
timeout /t 10 /nobreak >nul

REM Affichage du statut
echo === Deploiement termine ===
docker-compose ps

echo.
echo Application disponible sur: http://localhost:5001
echo Utilisateur admin: admin@flashnotify.local / admin123
echo.
echo Commandes utiles:
echo   deploy.bat logs    - Voir les logs
echo   deploy.bat stop    - Arreter les services
echo   deploy.bat restart - Redemarrer les services
echo   deploy.bat status  - Voir le statut
echo.

if "%1"=="logs" (
    docker-compose logs -f
) else if "%1"=="stop" (
    docker-compose down
    echo Services arretes
) else if "%1"=="restart" (
    docker-compose down
    docker-compose up -d
    echo Services redemarres
) else if "%1"=="status" (
    docker-compose ps
)

pause