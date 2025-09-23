from datetime import datetime
import os
import glob
import logging
from flask import Flask, request, jsonify, redirect, url_for
from config import COULEURS_LOCALISATION, LOCALISATION_COULEUR, APPAREIL_nom, LOCALISATION

# TODO : Utiliser le logger configuré dans config.py
# Exemple : logger = logging.getLogger(__name__)

app = Flask(__name__)
alertes = []

@app.route('/')
def accueil():
    # TODO : Ajouter un log INFO à chaque accès à la page d'accueil
    # Exemple : logger.info("Accès à la page d'accueil")
    return f"""
    <h1>Centre de Surveillance</h1>
    <p><strong>Alertes reçues :</strong> {len(alertes)}</p>
    <p><a href="/alertes">Voir toutes les alertes</a></p>
    <hr>
    <p><em>Serveur en attente d'alertes...</em></p>
    """

@app.route('/alerte', methods=['POST'])
def recevoir_alerte():
    try:
        data = request.get_json()

        if not data:
            # TODO : Ajouter un log WARNING si données manquantes
            # Exemple : logger.warning("Données JSON manquantes dans la requête")
            return jsonify({"status": "ERREUR", "message": "Données manquantes"}), 400

        alerte = {
            'timestamp_reception': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'donnees': data
        }
        alertes.append(alerte)

        # TODO : Ajouter un log INFO pour chaque alerte reçue
        # Exemple : logger.info(f"Alerte reçue de {data.get('source', 'Source inconnue')}, type : {data.get('type', 'Type inconnu')}")

        print(f"\n=== ALERTE #{len(alertes)} ===")
        print(f"Reçue : {alerte['timestamp_reception']}")
        print(f"Source : {data.get('source', 'Inconnue')}")
        print(f"Message : {data.get('message', 'Aucun message')}")

        # TODO : Ajouter un log DEBUG pour le suivi des alertes
        # Exemple : logger.debug(f"Alertes actuelles : {len(alertes)}")

        return jsonify({"status": "OK", "alerte_id": len(alertes)}), 200

    except Exception as e:
        # TODO : Ajouter un log EXCEPTION en cas d'erreur
        # Exemple : logger.exception("Erreur lors de la réception de l'alerte")
        return jsonify({"status": "ERREUR", "message": str(e)}), 400

@app.route('/alertes')
def lister_alertes():
    # TODO : Ajouter un log INFO à chaque accès à la liste des alertes
    # Exemple : logger.info("Accès à la page de liste des alertes")

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="3">
        <title>Historique des alertes</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .alerte { border: 2px solid; margin: 10px; padding: 15px; border-radius: 8px; }
            .alerte h3 { margin-top: 0; }
        </style>
    </head>
    <body>
    <h1>Historique des Alertes</h1>
    """

    if not alertes:
        html += "<p>Aucune alerte reçue.</p>"
    else:
        for i, alerte in enumerate(alertes, 1):
            localisation = alerte['donnees'].get('localisation', 'Inconnue')
            couleur_localisation = COULEURS_LOCALISATION.get(localisation, "black")
            type_alerte = alerte['donnees'].get('type', 'Inconnu')

            html += f"""
            <div class="alerte" style="border-color: {couleur_localisation};">
                <h3 style="color: {couleur_localisation};">Alerte #{i} - {type_alerte}</h3>
                <p><strong>Reçue :</strong> {alerte['timestamp_reception']}</p>
                <p><strong>Source :</strong> {alerte['donnees'].get('source', 'Inconnue')}</p>
                <p><strong>Message :</strong> {alerte['donnees'].get('message', 'Aucun message')}</p>
                <p><strong>Localisation :</strong> {localisation}</p>
            </div>
            """

    html += """
    <hr>
    <p><a href="/">Retour à l'accueil</a></p>
    </body>
    </html>
    """
    return html

@app.route('/reset', methods=['POST'])
def reset_alertes():
    """Route pour remettre à zéro les alertes (utile pour les tests)."""
    global alertes
    nb_alertes = len(alertes)
    alertes = []
    # TODO : Ajouter un log INFO après le reset
    # Exemple : logger.info(f"Reset des alertes effectué - {nb_alertes} alertes supprimées")
    return jsonify({"status": "OK", "message": f"{nb_alertes} alertes supprimées"}), 200

if __name__ == '__main__':
    # TODO : Ajouter un log INFO au démarrage du serveur
    # Exemple : logger.info("Démarrage du serveur de surveillance")
    print("Serveur de surveillance démarré sur http://localhost:5000")
    print("Appuyez sur Ctrl+C pour arrêter le serveur")

    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        # TODO : Ajouter un log INFO à l'arrêt du serveur
        # Exemple : logger.info("Arrêt du serveur demandé")
        print("\nArrêt du serveur.")