# Configuration de l'appareil - À compléter par chaque binôme
# ------------------------------------------------------------

# 1. Identifiant unique de l'appareil (choisir parmi RPi-01, RPi-02, RPi-03, etc.)
APPAREIL_ID = "RPi-XX"  # Remplacer XX par le numéro de votre Raspberry Pi

# 2. Nom de l'appareil (exemple : "Poste-RPi-01")
APPAREIL_nom = "Poste-RPi-XX"  # Remplacer XX par le numéro de votre Raspberry Pi

# 3. Localisation de l'appareil (choisir parmi la liste ci-dessous)
# Liste des localisations disponibles :
# - Direction
# - Accueil
# - Bureau commercial
# - Salle de réunion
# - Open space développement
# - Stockage matériel IT
LOCALISATION = "À compléter"  # Exemple : "Direction"

# 4. Couleur associée à la localisation (voir tableau ci-dessous)
# Tableau des couleurs par localisation :
# | Localisation              | Couleur   |
# |---------------------------|-----------|
# | Direction                 | red       |
# | Accueil                   | green     |
# | Bureau commercial         | green     |
# | Salle de réunion          | green     |
# | Open space développement  | orange    |
# | Stockage matériel IT      | red       |
# Si votre localisation n'est pas dans le tableau, définissez une couleur par défaut ici :
LOCALISATION_COULEUR = "black"  # Exemple : "red", "green", etc.

# 5. Type d'alerte (voir tableau ci-dessous)
# Tableau des types d'alerte par appareil :
# | Appareil  | Type d’alerte     |
# |-----------|------------------|
# | RPi-01    | intrusion        |
# | RPi-02    | accueil          |
# | RPi-03    | urgence système  |
# | RPi-04    | réglage système  |
# | RPi-05    | maintenance      |
# | RPi-06    | stockage         |
TYPE_ALERTE_APPAREIL = "À compléter"  # Exemple : "intrusion"

# Dictionnaire des couleurs par localisation (ne pas modifier)
COULEURS_LOCALISATION = {
    "Direction": "red",
    "Accueil": "green",
    "Bureau commercial": "green",
    "Salle de réunion": "green",
    "Open space développement": "orange",
    "Stockage matériel IT": "red"
}

# =============================================================================
# Configuration des logs - À ne pas modifier sauf indication de l'enseignant
# =============================================================================
import logging
import os
from logging.handlers import RotatingFileHandler

# Création du dossier "logs" s'il n'existe pas
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Le nom du fichier log est basé sur l'APPAREIL_ID (ex. RPi-01_application.log)
log_file_name = os.path.join(log_dir, f"{APPAREIL_ID}_application.log")

# Configuration de la rotation des logs : fichier max 1 Mo, conservation des 5 derniers fichiers
handler = RotatingFileHandler(
    log_file_name,
    maxBytes=1_000_000,   # Taille max du fichier (1 Mo)
    backupCount=5         # Nombre de fichiers conservés
)

# Configuration du logging : niveau INFO, format standard, affichage console + fichier
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Affichage dans la console
        handler                   # Écriture dans le fichier
    ]
)

# Création d'un logger global
logger = logging.getLogger()

# Message de démarrage pour vérifier que la configuration est bien chargée
logger.info(f"Configuration chargée pour {APPAREIL_ID} - {LOCALISATION}")