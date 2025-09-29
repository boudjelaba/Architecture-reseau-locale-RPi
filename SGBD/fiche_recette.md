# Fiche de recette - SGBD MariaDB

**Binôme** : [Noms]
**Date** : [Date]
**Version** : 1.0

---
## 1. Prérequis
| **ID** | **Description**                          | **Validé (✔/✘)** | **Commentaires**          |
|--------|------------------------------------------|------------------|---------------------------|
| PR01   | Raspberry Pi OS à jour                  | ✔                | `sudo apt update && upgrade` |
| PR02   | MariaDB installé et sécurisé             | ✔                | `mysql --version`         |
| PR03   | Accès distant activé                    | ✔                | `grep "bind-address" /etc/mysql/mariadb.conf.d/50-server.cnf` |

---
## 2. Tests fonctionnels

### 2.1 Configuration de la BDD publique
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T01         | Connexion utilisateur lecteur     | Accès en lecture seule                  | `mysql -u lecteur -p -e "USE projet_public; SELECT * FROM exemple;"` | Résultat de la requête | ✔ | 🟢 OK |
| T02         | Refus d'écriture                  | Tentative d'INSERT avec `lecteur`       | `mysql -u lecteur -p -e "USE projet_public; INSERT INTO exemple (data) VALUES ('test');"` | Erreur de permission | ✔ | 🟢 OK |

### 2.2 Configuration de la BDD privée
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T03         | Accès admin complet               | Droits complets sur `projet_prive`       | `mysql -u admin -p -e "USE projet_prive; SHOW TABLES;"` | Liste des tables | ✔ | 🟢 OK |
| T04         | Création de table                 | Création d'une table par `admin`        | `mysql -u admin -p -e "USE projet_prive; CREATE TABLE test (id INT);"` | Table créée | ✔ | 🟢 OK |

---
## 3. Tests d'accès distant
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T05         | Connexion depuis RPi2 (NAS)       | Accès à la BDD publique                  | `mysql -h <IP_RPi3> -u lecteur -p -e "USE projet_public; SELECT * FROM exemple;"` | Résultat de la requête | ✔ | 🟢 OK |
| T06         | Connexion depuis un PC client     | Accès à la BDD privée (admin)            | `mysql -h <IP_RPi3> -u admin -p -e "USE projet_prive; SHOW TABLES;"` | Liste des tables | ✔ | 🟢 OK |

---
## 4. Tests de robustesse
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T07         | Redémarrage de MariaDB            | Service redémarré proprement             | `sudo systemctl restart mysql`           | Service actif, BDD accessibles    | ✔                   | 🟢 OK      |
| T08         | Sauvegarde et restauration        | Sauvegarde et restauration de la BDD    | `mysqldump -u root -p projet_public > backup.sql` puis restauration | BDD restaurée sans erreur | ✔ | 🟢 OK |

---
## 5. Observations
- **Succès** : Les BDD publique et privée sont accessibles avec les bons droits.
- **Points à améliorer** :
  - Automatiser les sauvegardes quotidiennes via `cron`.
  - Documenter la procédure de restauration en cas de crash.

---
## 6. Validation globale
**Statut final** : 🟢 **Validé**

---
