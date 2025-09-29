# **Architecture réseau locale et services associés avec Raspberry Pi**

## Table des matières

- [**Architecture réseau locale et services associés avec Raspberry Pi**](#architecture-réseau-locale-et-services-associés-avec-raspberry-pi)
  - [Table des matières](#table-des-matières)
  - [1. Introduction / Contexte](#1-introduction--contexte)
  - [2. Objectifs](#2-objectifs)
  - [3. Répartition des tâches par groupe](#3-répartition-des-tâches-par-groupe)
    - [**Répartition des binômes et tâches – Groupe 1 (6 étudiants)**](#répartition-des-binômes-et-tâches--groupe-1-6-étudiants)
    - [**Répartition des binômes et tâches – Groupe 2 (5 étudiants)**](#répartition-des-binômes-et-tâches--groupe-2-5-étudiants)
    - [Remarques générales :](#remarques-générales-)
    - [Groupe 1 – RPi1 (modèle 3 B+) : Hotspot Wi-Fi + Connexion Internet (NAT)](#groupe-1--rpi1-modèle-3-b--hotspot-wi-fi--connexion-internet-nat)
      - [**Répartition du temps (estimation)**](#répartition-du-temps-estimation)
      - [**Étapes clés**](#étapes-clés)
    - [Groupe 2 – RPi2 (modèle 5): NAS local](#groupe-2--rpi2-modèle-5-nas-local)
      - [**Répartition du temps**](#répartition-du-temps)
      - [**Étapes clés**](#étapes-clés-1)
    - [Groupe 3 – RPi3 (modèle 5) : Serveur de base de données](#groupe-3--rpi3-modèle-5--serveur-de-base-de-données)
      - [**Répartition du temps**](#répartition-du-temps-1)
      - [**Étapes clés**](#étapes-clés-2)
  - [4. Interaction entre les groupes](#4-interaction-entre-les-groupes)
  - [5. Checklist finale par groupe](#5-checklist-finale-par-groupe)
    - [**Groupe 1 (Hotspot)**](#groupe-1-hotspot)
    - [**Groupe 2 (NAS)**](#groupe-2-nas)
    - [**Groupe 3 (BDD)**](#groupe-3-bdd)
  - [6. Besoins fonctionnels](#6-besoins-fonctionnels)
  - [7. Contraintes techniques](#7-contraintes-techniques)
  - [8. Décomposition en lots de travail](#8-décomposition-en-lots-de-travail)
  - [9. Livrables](#9-livrables)
  - [10. Critères de validation](#10-critères-de-validation)
    - [Compétences clés](#compétences-clés)


## 1. Introduction / Contexte

Dans le cadre d’une situation professionnelle simulée, un organisme souhaite déployer une **infrastructure réseau locale autonome**, basée sur des équipements Raspberry Pi, pour :

* Fournir un **accès réseau (Wi-Fi)**,
* Mettre en place un **partage de fichiers sécurisé (NAS)**,
* Installer un **système de gestion de base de données (SGBD)** pour la centralisation d’informations.

Ce réseau doit pouvoir fonctionner dans un environnement isolé (hors domaine, sans services centralisés) tout en étant capable de partager une **connexion Internet** si elle est disponible.

```
[Internet]
   |
[RPi1 - Hotspot/NAT]
   /     |     \
[RPi2] [RPi3] [PC Client]
NAS     SGBD
```

## 2. Objectifs

Ce projet a pour but de vous permettre :

* De **concevoir, mettre en œuvre et sécuriser une architecture réseau locale complète** ;
* De **déployer des services réseau** : NAS (partage de fichiers), base de données, hotspot Wi-Fi ;
* De maîtriser les outils de configuration réseau (iptables, hostapd, Samba, MariaDB) et les bonnes pratiques de sécurité (WPA2, droits utilisateurs, sauvegardes) ;
* D’**expérimenter le travail en équipe projet**, en coordination avec d'autres groupes techniques ;
* De développer les **compétences professionnelles transverses** liées à la gestion de projet, à l’autonomie technique et à la documentation ;
* De comprendre l’interdépendance des services réseau et l’importance de la documentation pour la maintenance et la collaboration.

---

## 3. Répartition des tâches par groupe

Les groupes devront s’assurer de l’**interopérabilité** de leurs solutions, avec possibilité de faire tester leur service par les autres RPi ou des PC clients.

- Chaque binôme doit **documenter ses choix techniques** (pourquoi Samba plutôt que NFS ? Pourquoi WPA2 plutôt que WPA3 ?) et **anticiper les tests croisés** avec les autres groupes.

### **Répartition des binômes et tâches – Groupe 1 (6 étudiants)**

| Binôme / Étudiant | RPi / Poste           | Tâches principales assignées                                                                 | Interdépendances |
| ----------------- | --------------------- | -------------------------------------------------------------------------------------------- |-------------------|
| Rafaël / Nathan   | RPi1 – Hotspot Wi-Fi  | Mise en place du hotspot sécurisé, DHCP, NAT, partage de connexion                           | RPi2 et RPi3 dépendent de ce service pour le réseau. |
| Noa / Axel        | RPi2 – Serveur NAS    | Installation de Samba, création des partages publics/privés, gestion des utilisateurs        |
| Charles / Teddy   | RPi3 – SGBD (MariaDB) | Déploiement de MariaDB, création des bases, gestion des droits, accès distant et sauvegardes |

### **Répartition des binômes et tâches – Groupe 2 (5 étudiants)**

| Binôme / Étudiant | RPi / Poste           | Tâches principales assignées                                                                 | Interdépendances |
| ----------------- | --------------------- | -------------------------------------------------------------------------------------------- |-------------------|
| Enzo / Tom        | RPi1 – Hotspot Wi-Fi  | Mise en place du hotspot sécurisé, DHCP, NAT, partage de connexion                           | RPi2 et RPi3 dépendent de ce service pour le réseau. |
| Armand / Luc      | RPi2 – Serveur NAS    | Installation de Samba, création des partages publics/privés, gestion des utilisateurs        |
| Louna             | RPi3 – SGBD (MariaDB) | Déploiement de MariaDB, création des bases, gestion des droits, accès distant et sauvegardes |

---

### Remarques générales :

* Chaque binôme (ou monôme) est responsable de :

  * La **documentation technique** de ses services ;
  * Un **script bash d’installation automatique** ;
  * Une **fiche de recette** pour valider la conformité fonctionnelle.
* Tous les postes devront être **interconnectés** via le réseau local du RPi1.
* **Tests croisés obligatoires** entre RPi : montage NAS depuis les autres machines, accès BDD à distance, etc.

### Groupe 1 – RPi1 (modèle 3 B+) : Hotspot Wi-Fi + Connexion Internet (NAT)

**Objectif** : Un hotspot Wi-Fi stable, sécurisé (WPA2), avec partage de connexion Internet (NAT).

**Conseil** : activer le refroidissement passif (dissipateur thermique + boîtier ventilé si possible), car le RPi 3 B+ peut chauffer légèrement en mode AP/NAT.

**Responsabilités :**

* Transformer le RPi en **point d’accès Wi-Fi** (hotspot).
* Connecter le RPi1 à Internet (Ethernet ou Wi-Fi).
* Activer le **partage de connexion (NAT + iptables)** pour que les autres RPi connectés au hotspot aient accès à Internet.
* Configurer un **DHCP local** (via `dnsmasq`).
* Sécuriser le réseau Wi-Fi (WPA2 minimum).

**Outils/Techno :**

* `hostapd`, `dnsmasq`, `iptables`, `netfilter-persistent`, etc.

#### **Répartition du temps (estimation)**

| Étape                     | Temps  | Détails                                                                 |
|---------------------------|--------|-------------------------------------------------------------------------|
| Préparation                | 1h     | Flasher la carte SD, mise à jour du système, installation des paquets.|
| Configuration hotspot      | 3h     | `hostapd`, `dnsmasq`, adressage IP fixe.                              |
| Configuration NAT          | 2h     | Règles `iptables`, test du partage Internet.                           |
| Tests et débogage          | 3h     | Vérification avec plusieurs clients, stabilité.                       |
| Documentation              | 1h     | Schéma réseau, commandes clés, captures d’écran.                     |

#### **Étapes clés**
1. **Installation** :
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install hostapd dnsmasq iptables
   sudo systemctl stop hostapd dnsmasq
   ```
2. **Configuration hotspot** :
   - [`hostapd.conf`](https://gist.github.com/.../hostapd.conf) (SSID: `ProjetRPi`, WPA2, canal 6).
   - [`dnsmasq.conf`](https://gist.github.com/.../dnsmasq.conf) (plage IP: 192.168.4.2-20).
3. **NAT** :
   ```bash
   echo 1 > /proc/sys/net/ipv4/ip_forward
   iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
   iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
   iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
   sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
   ```
4. **Tests** :
   - Se connecter avec un téléphone/PC, vérifier l’accès Internet.

---

### Groupe 2 – RPi2 (modèle 5): NAS local

**Objectif** : Un serveur NAS avec un partage public et un partage privé sécurisé.

**Conseil** : privilégier **Samba** pour une compatibilité maximale avec Windows/Linux/Mac. Séparer les partages publics/privés avec des droits ACL ou des users Samba.

**Responsabilités :**

* Se connecter au **hotspot du RPi1**.
* Installer et configurer un **serveur NAS** (ex: **Samba** ou **NFS**).
* Créer un **dossier partagé public** accessible à tous les clients.
* Créer un **dossier privé** contenant un répertoire par étudiant avec contrôle d’accès (login/mdp différents).
* Monter ces dossiers automatiquement côté client (autres RPi).

**Outils/Techno :**

* `samba`, `nfs-kernel-server`, gestion des permissions Linux, `autofs` (si nécessaire).


#### **Répartition du temps**

| Étape                     | Temps  | Détails                                                                 |
|---------------------------|--------|-------------------------------------------------------------------------|
| Préparation                | 1h     | Installation de Samba, création des dossiers.                        |
| Configuration Samba        | 4h     | Édition de `smb.conf`, gestion des utilisateurs et permissions.       |
| Tests de montage           | 3h     | Montage depuis Linux/Windows, vérification des droits.                |
| Automatisation             | 2h     | Script d’installation automatique (optionnel si temps).              |
| Documentation              | 1h     | Schéma, commandes, captures.                                            |

#### **Étapes clés**

1. **Installation** :
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install samba
   ```
2. **Configuration** :
   - [`smb.conf`](https://gist.github.com/.../smb.conf) (partages public/prive).
   - Créer les utilisateurs :
     ```bash
     sudo useradd etudiant1
     sudo smbpasswd -a etudiant1
     ```
3. **Tests** :
   - Depuis un client Linux :
     ```bash
     sudo apt install cifs-utils
     sudo mount -t cifs //<IP_RPi2>/public /mnt/nas -o guest
     sudo mount -t cifs //<IP_RPi2>/prive /mnt/nas_prive -o username=etudiant1
     ```

---

### Groupe 3 – RPi3 (modèle 5) : Serveur de base de données

**Objectif** : Un serveur MariaDB avec une base publique (lecture seule) et une base privée (droits personnalisés).

**Conseil** : placer les fichiers de données (`/var/lib/mysql` ou `/var/lib/postgresql`) sur un disque SSD (clé USB) via USB 3.0 pour de meilleures performances.

**Responsabilités :**

* Se connecter au **hotspot du RPi1**.
* Installer un **SGBD** (MariaDB ou PostgreSQL).
* Créer **deux bases de données** :

  1. Une base publique d'exemple (lecture seule).
  2. Une base privée où chaque étudiant a des **droits personnalisés** (lecture/écriture sur certaines tables).
* Gérer les utilisateurs, droits d'accès, sauvegardes.

**Outils/Techno :**

* `mariadb-server` ou `postgresql`, `phpmyadmin` (optionnel), `mysql` CLI ou PGAdmin.

#### **Répartition du temps**
| Étape                     | Temps  | Détails                                                                 |
|---------------------------|--------|-------------------------------------------------------------------------|
| Installation MariaDB       | 2h     | Installation, sécurisation, configuration de base.                    |
| Création BDD/utilisateurs | 3h     | Script SQL pour créer BDD, tables, utilisateurs.                       |
| Tests de connexion         | 3h     | Connexion depuis un autre RPi, vérification des droits.               |
| Sauvegarde/automatisation  | 2h     | Script de sauvegarde, cron (optionnel).                                |
| Documentation              | 1h     | Schéma, commandes, captures.                                            |

#### **Étapes clés**
1. **Installation** :
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install mariadb-server
   sudo mysql_secure_installation
   ```
2. **Configuration** :
   - Autoriser l’accès distant :
     ```bash
     sudo mysql -e "GRANT ALL ON *.* TO 'admin'@'%' IDENTIFIED BY 'admin123'; FLUSH PRIVILEGES;"
     ```
   - Éditer `/etc/mysql/mariadb.conf.d/50-server.cnf` : commenter `bind-address`.
3. **Création BDD** :
   ```sql
   CREATE DATABASE projet;
   USE projet;
   CREATE TABLE public (id INT AUTO_INCREMENT PRIMARY KEY, data VARCHAR(255));
   INSERT INTO public (data) VALUES ('Test public');
   CREATE USER 'lecteur'@'%' IDENTIFIED BY 'lecteur123';
   GRANT SELECT ON projet.public TO 'lecteur'@'%';
   CREATE USER 'admin'@'%' IDENTIFIED BY 'admin123';
   GRANT ALL ON projet.* TO 'admin'@'%';
   FLUSH PRIVILEGES;
   ```
4. **Tests** :
   - Depuis un autre RPi :
     ```bash
     mysql -h <IP_RPi3> -u lecteur -p
     ```

---

## 4. Interaction entre les groupes

* **RPi2 et RPi3 se connectent au hotspot de RPi1** pour réseau + Internet.
* **RPi2 NAS est monté sur RPi3** pour stocker par exemple les backups des BDD ou logs.
* **Tester les accès croisés** : montage du NAS depuis un client RPi ou PC externe, connexion BDD depuis différents clients, etc.

  | Service source | Service cible | Protocole/Port | Exemple de commande de test |
  |-----------------|---------------|----------------|-----------------------------|
  | RPi1 (Hotspot)  | RPi2 (NAS)    | DHCP, ICMP     | `ping 192.168.4.2`           |
  | RPi3 (SGBD)     | RPi2 (NAS)    | SMB (445)      | `smbclient -L //192.168.4.2` |
  | PC Client       | RPi3 (SGBD)   | MySQL (3306)   | `mysql -h 192.168.4.3 -u lecteur -p` |

- **Tests d’intégration** :
  - Chaque groupe doit valider que son service est accessible depuis **au moins un autre RPi et un PC client** (Windows ou Linux).

---

## 5. Checklist finale par groupe

### **Groupe 1 (Hotspot)**

- [ ] Hotspot visible et accessible (SSID, mot de passe).
- [ ] Clients obtiennent une IP via DHCP.
- [ ] Accès Internet fonctionnel via NAT.
- [ ] Documentation complète (schéma, commandes, captures).
- [ ] (optionnel) Les services inutiles sont désactivés (`sudo systemctl list-units --type=service`).
- [ ] (optionnel) Les logs sont activés et consultables (`journalctl -u hostapd`, `tail -f /var/log/samba/log.smbd`).

### **Groupe 2 (NAS)**

- [ ] Partage public accessible sans authentification.
- [ ] Partage privé accessible avec utilisateur/mot de passe.
- [ ] Montage réussi depuis un client Linux/Windows.
- [ ] Documentation complète.
- [ ] (optionnel) Les services inutiles sont désactivés (`sudo systemctl list-units --type=service`).
- [ ] (optionnel) Les logs sont activés et consultables (`journalctl -u hostapd`, `tail -f /var/log/samba/log.smbd`).

### **Groupe 3 (BDD)**

- [ ] BDD accessible depuis un autre RPi.
- [ ] Droits différenciés (lecteur vs admin) fonctionnels.
- [ ] Sauvegarde de la BDD testée.
- [ ] Un script de sauvegarde automatique de la BDD est fonctionnel et testé.
- [ ] Documentation complète.
- [ ] (optionnel) Les services inutiles sont désactivés (`sudo systemctl list-units --type=service`).
- [ ] (optionnel) Les logs sont activés et consultables (`journalctl -u hostapd`, `tail -f /var/log/samba/log.smbd`).

---

## 6. Besoins fonctionnels

| Code    | Fonction attendue                                                                            |
| ------- | -------------------------------------------------------------------------------------------- |
| **F01** | Le système doit permettre à plusieurs utilisateurs de se connecter en Wi-Fi localement       |
| **F02** | Le réseau local doit fournir un accès à Internet via NAT si le RPi est connecté en Ethernet  |
| **F03** | Un service de partage de fichiers doit être accessible par tous les clients (dossier public) |
| **F04** | Chaque utilisateur doit avoir un espace privé protégé par identifiant/mot de passe           |
| **F05** | Un service SGBD doit être installé, avec au moins deux bases accessibles par le réseau       |
| **F06** | Les services doivent être accessibles depuis les autres RPi ou un PC client                  |
| **F07** | Chaque service doit disposer d’un script d’installation automatique                          |
| **F08** | Une fiche de recette doit valider la conformité fonctionnelle de chaque service              |

---

## 7. Contraintes techniques

| Code    | Contraintes                                                                            |
| ------- | -------------------------------------------------------------------------------------- |
| **CT1** | Les RPi doivent fonctionner sous Raspberry Pi OS (Lite ou Desktop)                     |
| **CT2** | L’adressage IP doit être maîtrisé (fixe pour serveurs, DHCP pour clients)              |
| **CT3** | Le service Wi-Fi doit être sécurisé par WPA2                                           |
| **CT4** | Aucun service externe (cloud, DNS dynamique, etc.) ne doit être utilisé                |
| **CT5** | Les scripts doivent être compatibles bash                                              |
| **CT6** | Le projet doit être réalisable dans un délai de 10 à 16 heures                         |
| **CT7** | Aucun service superflu ne doit être activé sur les RPi (principe de sécurité minimale) |
| **CT8** | (optionnel) Les adresses IP des serveurs (RPi2, RPi3) doivent être **fixes** (via `/etc/dhcpcd.conf` ou réservation DHCP).
| **CT9** | (optionnel) Les noms d’hôte doivent être configurés (`hostnamectl`) et résolus localement (via `/etc/hosts` sur chaque machine).

---

## 8. Décomposition en lots de travail

| Lot     | Groupe   | Objectifs                                                                           |
| ------- | -------- | ----------------------------------------------------------------------------------- |
| **LT1** | Groupe 1 | Mise en place d’un hotspot Wi-Fi sécurisé + partage de connexion NAT                |
| **LT2** | Groupe 2 | Déploiement d’un serveur NAS avec gestion des utilisateurs                          |
| **LT3** | Groupe 3 | Déploiement d’un serveur SGBD avec configuration réseau + BDD                       |
| **LT4** | Tous     | Rédaction des scripts d’automatisation, documentation, fiche recette, tests croisés |
| **LT5** | Tous     | Tests croisés, résolution des problèmes d’interopérabilité, finalisation de la documentation. |

---

## 9. Livrables

Chaque groupe devra fournir :

| Type                 | Contenu                                                      |
| -------------------- | ------------------------------------------------------------ |
| **Script**           | Script bash d’installation ou de configuration automatisée (`hostapd.conf`, `smb.conf`, `my.cnf`, etc.)  |
| **Documentation**    | Rapport technique, schéma réseau, captures de configuration  |
| **Fiche de recette** | Liste de tests fonctionnels réalisés (résultats, validation) |
| **Présentation**     | Diaporama et démonstration en fin de projet                  |

- **Script** :
  - "Le script doit **afficher des messages clairs** (ex: `Échec : le paquet hostapd n’est pas installé`) et **proposer des solutions** (ex: `sudo apt install hostapd`)."
  - "Inclure un **mode debug** (ex: `./script.sh --debug` pour afficher les logs)."
- **Documentation** :
  - "Fournir un **guide de dépannage** (ex: que faire si le hotspot n’est pas visible ? Si le montage NAS échoue ?)."
- **Fiche de recette** :
  - "Utiliser le **format Markdown** fourni en exemple (avec statuts OK/Partiel/Échec)."

* Un point d’avancement sera réalisé à mi-parcours.

  - "À mi-parcours : schéma réseau validé, services de base fonctionnels (hotspot, partage public, BDD accessible).

---

## 10. Critères de validation

* Fonctionnalité opérationnelle du service (F01 à F08)
* Conformité aux contraintes techniques (CT1 à CT7)
* Qualité du script et de la documentation
* Respect du planning et du travail en équipe
* Capacité à présenter, expliquer, justifier les choix techniques

- **Critère "Collaboration"** :
  - Capacité à **expliquer son service aux autres groupes** et à les aider à le tester.
- **Critère "Robustesse" (optionnel)** :
  - Les services doivent **redémarrer automatiquement** après un reboot (`systemctl enable hostapd`).
- **Critère "Performance" (souhaitable)** :
  - Le NAS doit permettre un transfert de fichiers > **5 Mo/s** (test avec `dd` ou `scp`).

### Compétences clés

| Compétence | Activités associées | Exemples dans le mini‑projet | Critères d’évaluation |
|------------|---------------------|----------------------------------------|-----------------------|
| **C05 : Concevoir un système informatique** | R2 (Installation et qualification), D1 (Analyse cahier des charges), D2 (Conception de solutions) | - Concevoir l’architecture réseau locale (Hotspot, NAS, BDD) <br> - Formaliser un schéma réseau clair <br> - Rédiger un plan de services (qui fournit quoi, quels clients) | - Architecture cohérente et fonctionnelle <br> - Documentation claire (schéma + services) |
| **C09 : Installer un réseau informatique** | R2 (Installation), R3 (Exploitation) | - Installer et configurer `hostapd` et `dnsmasq` pour le Hotspot <br> - Installer Samba et valider les partages <br> - Installer MariaDB/PostgreSQL et assurer la connexion réseau <br> - Vérifier que tous les RPi communiquent entre eux | - Services installés et opérationnels <br> - Respect des bonnes pratiques de configuration |
| **C06 : Valider un système informatique** | R2 (Recettage), D2 (Tests), R3 (Suivi exploitation) | - Réaliser des tests croisés (connexion Wi-Fi, accès NAS et BDD depuis client) <br> - Établir une fiche de recette validant chaque service <br> - Présenter et démontrer le système en fonctionnement | - Résultats des tests conformes au cahier des charges <br> - Fiche de recette complète <br> - Démonstration fluide et argumentée |
 
- **C05** couvre la *conception* (schéma, organisation, planification).  
- **C09** couvre l’*installation/mise en service* des RPi et services.  
- **C06** couvre la *validation* via tests, fiches de recette, et démo finale.  

---