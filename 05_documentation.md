# Documentation Technique – [Nom du service]

## 1. Présentation

**Service installé** : [Hotspot Wi-Fi / NAS / Base de données]  
**Nom du groupe** : Groupe 1 - Binôme .../...  
**Date d’installation** : [JJ/MM/AAAA]

---

## 2. Matériel utilisé

- Raspberry Pi modèle : [3B+ / 5]
- Support de stockage : [SD / SSD / Clé USB]
- Connexion : [Ethernet / Wi-Fi]
- Système : Raspberry Pi OS Lite/Desktop

---

## 3. Configuration réseau

- Adresse IP : `192.168.4.X` (fixe / DHCP)
- Masque : `255.255.255.0`
- Passerelle : `192.168.4.1`
- DNS : [local / externe]

---

## 4. Services installés

### Hotspot Wi-Fi
- SSID : `ProjetRPi`
- Mot de passe : `raspberry`
- Interface : `wlan0`

### NAS (exemple)
- Partage public : `/srv/samba/public`
- Partage privé : `/srv/samba/prive`
- Utilisateurs : `etudiant1`, `etudiant2`

### Base de données
- SGBD : MariaDB / PostgreSQL
- Utilisateurs créés : `lecteur`, `admin`
- Bases de données : `projet`, `test`

---

## 5. Scripts utilisés

- `script_install.sh` : script d’installation automatique
- [Autres scripts de sauvegarde, montage automatique, etc.]

---

## 6. Schéma réseau

> *Inclure un schéma du réseau local avec les adresses IP, services, liaisons.*

---

## 7. Problèmes rencontrés

- 🔴 Hostapd ne démarrait pas → corrigé en modifiant `country_code=FR`
- 🔴 Problème de droits Samba sur partage privé → corrigé avec ACL

---

## 8. Captures

> Captures d’écran ou terminal illustrant :
- L’installation
- Le fonctionnement
- Les erreurs résolues

---

## 9. Auteurs

- ...
- ...