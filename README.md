# Systeme-Alerte-Connecte-avec-Raspberry-Pi


```python
html += f"""
            <div class="alerte" style="border-color: {couleur_localisation};">
                <h3 style="color: {couleur_localisation};">Alerte #{i} - {type_alerte}</h3>
                <p><strong>Reçue :</strong> {alerte['timestamp_reception']}</p>
                <p><strong>Source :</strong> {alerte['donnees'].get('source', 'Inconnue')}</p>
                <p><strong>Message :</strong> {alerte['donnees'].get('message', 'Aucun message')}</p>
                <p><strong>Utilisation CPU :</strong> {alerte['donnees'].get('system_info', {}).get('cpu_usage', 'N/A')}%</p>
                <p><strong>Utilisation mémoire :</strong> {alerte['donnees'].get('system_info', {}).get('memory_usage', 'N/A')}%</p>
                <p><strong>Température :</strong> {alerte['donnees'].get('temperature', 'N/A')} °C</p>
                <p><strong>Localisation :</strong> {localisation}</p>
                <p><strong>IP source :</strong> {alerte['donnees'].get('ip_source', 'Inconnue')}</p>
            </div>
            """
```

## **TP : Système d’Alerte Connecté avec Raspberry Pi**

---

## Prérequis et Remédiation

### **Acquis de la séquence 2 (requis pour ce TP)**

- **Installation et configuration Raspberry Pi** (séance 2.2)
- **Premiers pas Linux** (séance 2.3)
  - Commandes shell de base (navigation, fichiers, droits)
  - Utilisation des éditeurs (nano, geany)
  - Exécution de programmes Python
- **Services réseau sur RPi** (séance 2.4)
  - Installation et configuration Flask

### **Acquis des séquences précédentes**
- **Séquence 1 - Bases de données**
  - Concepts de client-serveur
  - Manipulation de données structurées
- **Programmation Python** (BTS 1ère année)
  - Variables, boucles, conditions, fonctions
  
---

## Savoirs Liés

- Adressage IP et configuration réseau
- Architecture des systèmes embarqués (ARM vs x86)
- Audit et surveillance des systèmes

---

### Compétences visées

| Code | Compétence | Niveau visé |
|------|------------|-------------|
| **C11** | Maintenir un réseau informatique  | 2 |

### Activités et Tâches

| **Activité** | **Code Tâche** | **Intitulé de la tâche** | **Mise en œuvre dans le TP** |
|--------------|----------------|--------------------------|------------------------------|
| **R3 - Exploitation et maintien en condition opérationnelle** | R3-T3 | Supervision de l’état du réseau dans son périmètre | Analyse des dysfonctionnements et codes d'erreur |
| **R5 - Maintenance des réseaux informatiques** | R5-T4 | Réalisation de diagnostics et d’interventions de maintenance curative | Surveillance du fonctionnement du système et logs  |

---

## Objectifs

- Envoyer une alerte simulée via HTTP POST.
- Observer l’interaction entre système embarqué et serveur réseau.
- Déployer un serveur Flask recevant et affichant des alertes.

---

### Matériel nécessaire :

* Raspberry Pi (un par binôme, OS à jour)
* 1 bouton (ou même clavier → simulation via `input()`)
* Accès réseau (filaire ou Wi-Fi)
* Python + dépendances :
  ```bash
  pip3 install requests flask
  ```

---

### Contexte  :

> "Une petite entreprise souhaite équiper ses bureaux d’un **système de bouton d’urgence connecté**. En cas d’incident (incendie, intrusion...), l’utilisateur appuie sur un bouton physique et **envoie automatiquement un message d’alerte à un serveur distant (poste de sécurité)**."

Le système doit être **léger**, **réactif**, et pouvoir être **déployé facilement** sur d’autres Raspberry Pi.

---

## Bouton

```python
# test_composants.py
import RPi.GPIO as GPIO
import time

# Configuration GPIO
BUTTON_PIN = 17
LED_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

print("=== Test des Composants ===")
print("Appuyez sur le bouton (Ctrl+C pour quitter)")

try:
    while True:
        # Lecture bouton (LOW = pressé avec pull-up)
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("Bouton détecté !")
            GPIO.output(LED_PIN, GPIO.HIGH)  # Allumer LED
            time.sleep(0.5)
            GPIO.output(LED_PIN, GPIO.LOW)   # Éteindre LED
            
            # Anti-rebond simple
            time.sleep(0.3)
        
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("\nArrêt du test")
finally:
    GPIO.cleanup()
```
