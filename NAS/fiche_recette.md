# Fiche de recette - Serveur NAS (Samba)

**Binôme** : [Noms]
**Date** : [Date]
**Version** : 1.0

---
## 1. Prérequis
| **ID** | **Description**                          | **Validé (✔/✘)** | **Commentaires**          |
|--------|------------------------------------------|------------------|---------------------------|
| PR01   | Raspberry Pi OS à jour                  | ✔                | `sudo apt update && upgrade` |
| PR02   | Paquet `samba` installé                  | ✔                | `apt list --installed | grep samba` |
| PR03   | Dossiers `/srv/samba/public` et `/srv/samba/private` existent | ✔ | `ls -l /srv/samba` |

---
## 2. Tests fonctionnels

### 2.1 Configuration du partage public
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T01         | Dossier public accessible         | Accès en lecture/écriture sans authentification | `smbclient //localhost/public -N -c "ls"` | Liste des fichiers                | ✔                   | 🟢 OK      |
| T02         | Création de fichier               | Création d'un fichier depuis un client  | `touch /srv/samba/public/test.txt`        | Fichier créé                      | ✔                   | 🟢 OK      |

### 2.2 Configuration du partage privé
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T03         | Accès refusé sans authentification | Tentative de connexion anonyme          | `smbclient //localhost/private -N -c "ls"` | Accès refusé                       | ✔                   | 🟢 OK      |
| T04         | Accès autorisé avec utilisateur   | Connexion avec `etudiant1`               | `smbclient //localhost/private -U etudiant1 -c "ls"` | Liste des fichiers | ✔ | 🟢 OK |

---
## 3. Tests de montage depuis un client
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T05         | Montage du partage public (Linux) | Montage depuis un client Linux          | `sudo mount -t cifs //<IP_RPi>/public /mnt/nas_public -o guest` | Dossier monté, accessible | ✔ | 🟢 OK |
| T06         | Montage du partage privé (Linux)  | Montage avec authentification           | `sudo mount -t cifs //<IP_RPi>/private /mnt/nas_private -o username=etudiant1` | Dossier monté, accessible | ✔ | 🟢 OK |

---
## 4. Tests de robustesse
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T07         | Redémarrage du service Samba     | Redémarrage propre de Samba              | `sudo systemctl restart smbd`            | Service actif, partages accessibles | ✔ | 🟢 OK |
| T08         | Reboot du RPi                     | Redémarrage complet du RPi               | `sudo reboot`                            | Partages disponibles après reboot | ✔ | 🟢 OK |

---
## 5. Observations
- **Succès** : Les partages public et privé sont fonctionnels et sécurisés.
- **Points à améliorer** :
  - Automatiser le montage des partages côté client via `/etc/fstab`.
  - Ajouter un quota disque pour les utilisateurs du partage privé.

---
## 6. Validation globale
**Statut final** : 🟢 **Validé**

---
