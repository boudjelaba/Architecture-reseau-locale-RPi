# Systeme-Alerte-Connecte-avec-Raspberry-Pi


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
