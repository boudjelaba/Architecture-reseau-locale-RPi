import MockGPIO as GPIO
import time
import requests
import json
from datetime import datetime
import socket
import threading
import psutil
import logging
from config import (APPAREIL_ID, APPAREIL_nom, LOCALISATION, LOCALISATION_COULEUR, TYPE_ALERTE_APPAREIL)

# TODO : Utiliser le logger configuré dans config.py
# Exemple : logger = logging.getLogger(__name__)

# Configuration GPIO (simulée)
BUTTON_PIN = 17
LED_PIN = 27
SERVEUR_URL = "http://localhost:5000/alerte"

# Initialisation GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

def obtenir_info_systeme():
    """Retourne des informations sur l'état du système."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        # TODO : Ajouter un log DEBUG pour tracer ces informations
        # Exemple : logger.debug(f"Info système récupérées - CPU: {cpu_usage}%, RAM: {memory_usage}%")
        return {
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage
        }
    except Exception as e:
        # TODO : Ajouter un log ERROR en cas d'erreur
        # Exemple : logger.error(f"Erreur lors de la récupération des informations système : {e}")
        return {}

def obtenir_temperature():
    """Retourne la température du Raspberry Pi en °C."""
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000.0
        # TODO : Ajouter un log DEBUG pour tracer la température
        # Exemple : logger.debug(f"Température récupérée : {temp}°C")
        return round(temp, 2)
    except Exception as e:
        # TODO : Ajouter un log ERROR en cas d'erreur
        # Exemple : logger.error(f"Erreur lors de la récupération de la température : {e}")
        return None

def obtenir_localisation():
    """Retourne la localisation de l'appareil."""
    return LOCALISATION

def obtenir_ip_locale():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        # TODO : Ajouter un log DEBUG pour tracer l'IP locale
        # Exemple : logger.debug(f"IP locale détectée : {ip}")
        return ip
    except Exception as e:
        # TODO : Ajouter un log WARNING en cas d'erreur
        # Exemple : logger.warning(f"Impossible de déterminer l'IP locale : {e}")
        return "IP inconnue"

def clignoter_led(nb_fois=3, duree=0.2):
    """Fait clignoter la LED un nombre de fois donné."""
    # TODO : Ajouter un log DEBUG pour tracer le clignotement
    # Exemple : logger.debug(f"Clignotement LED : {nb_fois} fois, durée {duree}s")
    for _ in range(nb_fois):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(duree)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(duree)

def envoyer_alerte():
    """Envoie une alerte au serveur de surveillance."""
    data = {
        "message": "Alerte d'urgence déclenchée !",
        "date_heure": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "source": APPAREIL_ID,
        "nom": APPAREIL_nom,
        "ip_source": obtenir_ip_locale(),
        "type": TYPE_ALERTE_APPAREIL,
        "system_info": obtenir_info_systeme(),
        "temperature": obtenir_temperature(),
        "localisation": obtenir_localisation(),
    }

    # TODO : Ajouter un log INFO avant l'envoi de l'alerte
    # Exemple : logger.info(f"Envoi de l'alerte de type : {TYPE_ALERTE_APPAREIL} depuis {APPAREIL_ID}")
    GPIO.output(LED_PIN, GPIO.HIGH)
    try:
        response = requests.post(SERVEUR_URL, json=data, timeout=3)

        if response.status_code == 200:
            # TODO : Ajouter un log INFO en cas de succès
            # Exemple : logger.info("Alerte envoyée avec succès !")
            print("Alerte envoyée avec succès !")
            GPIO.output(LED_PIN, GPIO.LOW)
            clignoter_led(2, 0.15)
        else:
            # TODO : Ajouter un log WARNING en cas d'erreur serveur
            # Exemple : logger.warning(f"Erreur lors de l'envoi de l'alerte, code serveur {response.status_code}")
            print(f"Erreur : Code serveur {response.status_code}")
            GPIO.output(LED_PIN, GPIO.LOW)
            clignoter_led(4, 0.1)
    except requests.exceptions.ConnectionError:
        # TODO : Ajouter un log ERROR en cas de connexion impossible
        # Exemple : logger.error("Erreur de connexion, serveur injoignable")
        print("Serveur injoignable")
        GPIO.output(LED_PIN, GPIO.LOW)
        clignoter_led(6, 0.3)
    except Exception as e:
        # TODO : Ajouter un log EXCEPTION en cas d'erreur inattendue
        # Exemple : logger.exception("Une exception s'est produite lors de l'envoi de l'alerte")
        print(f"Exception : {e}")
        GPIO.output(LED_PIN, GPIO.LOW)
        clignoter_led(5, 0.2)

def ecoute_bouton():
    """Thread d'écoute du bouton GPIO."""
    derniere_alerte = 0
    # TODO : Ajouter un log INFO au démarrage de l'écoute
    # Exemple : logger.info("Démarrage de l'écoute du bouton GPIO")

    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            now = time.time()
            if now - derniere_alerte > 3:
                # TODO : Ajouter un log INFO lors de l'activation du bouton
                # Exemple : logger.info("Bouton d'urgence activé (GPIO)")
                print("\nBouton d'urgence activé (GPIO)")
                envoyer_alerte()
                derniere_alerte = now
        time.sleep(0.1)

def interface_simulation():
    """Interface utilisateur pour la simulation."""
    print("\n--- Interface de simulation ---")
    print("Appuyez sur [Entrée] pour simuler un appui bouton.")
    print("Tapez 'q' puis [Entrée] pour quitter.\n")
    while True:
        user_input = input(">>> ")
        if user_input.lower() == 'q':
            # TODO : Ajouter un log INFO à l'arrêt
            # Exemple : logger.info("Arrêt demandé par l'utilisateur")
            print("Arrêt demandé.")
            break
        else:
            # TODO : Ajouter un log INFO lors de la simulation d'appui
            # Exemple : logger.info("Simulation d'appui bouton par l'utilisateur")
            print("[SIMULATION] Appui bouton simulé.")
            GPIO.simulate_button_press(BUTTON_PIN)
            time.sleep(0.5)
            GPIO.simulate_button_release(BUTTON_PIN)

# Programme principal
if __name__ == "__main__":
    print("=== SYSTÈME D'ALERTE D'URGENCE (SIMULATION) ===")
    print(f"Matériel : {APPAREIL_ID}")
    print(f"Serveur : {SERVEUR_URL}")
    print(f"IP locale : {obtenir_ip_locale()}")
    print("--------------------------------------------------")

    # TODO : Ajouter un log INFO au démarrage du système
    # Exemple : logger.info(f"Démarrage du système d'alerte - {APPAREIL_ID}")

    try:
        # Démarrer le thread d'écoute GPIO
        thread_gpio = threading.Thread(target=ecoute_bouton)
        thread_gpio.daemon = True
        thread_gpio.start()

        # Interface utilisateur
        interface_simulation()
    except KeyboardInterrupt:
        # TODO : Ajouter un log INFO en cas d'interruption clavier
        # Exemple : logger.info("Interruption clavier reçue. Fin du programme.")
        print("\nInterruption clavier reçue. Fin du programme.")
    finally:
        GPIO.cleanup()
        # TODO : Ajouter un log INFO à la fin du programme
        # Exemple : logger.info("Nettoyage GPIO terminé")
        print("GPIO nettoyé. Fin.")