# Checklist de suivi par séance

## **Séance 1 (4h) — Installation & préparation**

### Groupe 1 (Hotspot Wi-Fi + DHCP)

* [ ] Flasher carte SD, installer Raspberry Pi OS
* [ ] Mise à jour système (`apt update && upgrade`)
* [ ] Installer `hostapd`, `dnsmasq`, `iptables`
* [ ] Configurer adresse IP fixe pour wlan0
* [ ] Éditer `hostapd.conf` (SSID, canal, WPA2)
* [ ] Configurer `dnsmasq.conf` pour DHCP
* [ ] Tester la diffusion du hotspot (SSID visible)

### Groupe 2 (NAS Samba)

* [ ] Flasher carte SD, installer Raspberry Pi OS
* [ ] Mise à jour système (`apt update && upgrade`)
* [ ] Installer Samba (`sudo apt install samba`)
* [ ] Créer dossiers partagés (public + privé)
* [ ] Initialiser configuration Samba minimale (`smb.conf`)
* [ ] Créer les premiers utilisateurs Samba
* [ ] Tester accès local (via `smbclient` ou partage Windows)

### Groupe 3 (SGBD)

* [ ] Flasher carte SD, installer Raspberry Pi OS
* [ ] Mise à jour système (`apt update && upgrade`)
* [ ] Installer MariaDB ou PostgreSQL
* [ ] Sécuriser installation (`mysql_secure_installation` ou équivalent)
* [ ] Démarrer le service SGBD
* [ ] Préparer accès distant (modifier `bind-address` si nécessaire)
* [ ] Vérifier accès local au SGBD

---

## **Séance 2 (3h) — Configuration avancée & tests**

### Groupe 1 (NAT et sécurisation)

* [ ] Configurer le partage de connexion (iptables, NAT)
* [ ] Activer forwarding IPv4
* [ ] Tester accès Internet depuis clients connectés au hotspot
* [ ] Valider sécurité WPA2

### Groupe 2 (Samba avancé)

* [ ] Finaliser `smb.conf` (partages public + privés, ACL)
* [ ] Créer utilisateurs Samba avec mots de passe
* [ ] Tester montage Samba depuis clients Linux et Windows
* [ ] Gérer droits d’accès pour dossiers privés

### Groupe 3 (Bases & droits)

* [ ] Créer bases de données (publique et privée)
* [ ] Créer utilisateurs SGBD avec droits différenciés (lecture/écriture)
* [ ] Tester connexions clients avec différents utilisateurs
* [ ] Effectuer tests CRUD (Create, Read, Update, Delete)

---

## **Séance 3 (4h) — Tests croisés, automatisation et documentation**

### Tous groupes

* [ ] Monter NAS de RPi2 sur RPi3 (backup BDD, logs)
* [ ] Tester accès BDD depuis RPi2 et autres clients
* [ ] Tester stabilité et accès Internet sur tous les RPi
* [ ] Écrire scripts bash d’installation/configuration automatisée
* [ ] Documenter schémas réseau, commandes clés, résultats tests
* [ ] Rédiger fiche recette (tests fonctionnels + validation)
* [ ] Préparer diaporama et démonstration finale

---

## **Séance 4 (3h) — Revue & présentation**

* [ ] Corriger éventuels bugs restants
* [ ] Finaliser documentation
* [ ] Répéter la présentation orale
* [ ] Valider la conformité fonctionnelle globale
* [ ] Présentation orale et démo
