# Fiche de recette - Hotspot Wi-Fi + NAT

**Binôme** : [Noms]
**Date** : [Date]
**Version** : 1.0

---
## 1. Prérequis
| **ID** | **Description**                          | **Validé (✔/✘)** | **Commentaires**          |
|--------|------------------------------------------|------------------|---------------------------|
| PR01   | Raspberry Pi OS à jour                  | ✔                | `sudo apt update && upgrade` |
| PR02   | Paquets `hostapd`, `dnsmasq` installés  | ✔                | Voir script d'installation |
| PR03   | Interface Wi-Fi (`wlan0`) disponible     | ✔                | `iwconfig`                |

---
## 2. Tests fonctionnels

### 2.1 Configuration du Hotspot
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T01         | Hotspot visible                   | Le SSID "ProjetRPi" est visible          | `iwconfig` ou recherche Wi-Fi (smartphone/PC) | SSID détecté                     | ✔                   | 🟢 OK      |
| T02         | Connexion possible                | Connexion avec mot de passe WPA2         | Tentative de connexion depuis un client | Connexion établie, IP attribuée   | ✔                   | 🟢 OK      |
| T03         | Adressage IP correct              | Plage DHCP respectée (192.168.4.2-20)    | `ip a` sur le client                     | IP dans la plage DHCP             | 192.168.4.5         | 🟢 OK      |

### 2.2 Partage de connexion (NAT)
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T04         | Accès Internet                    | Ping vers 8.8.8.8 depuis un client      | `ping 8.8.8.8`                           | Réponse ICMP                       | ✔                   | 🟢 OK      |
| T05         | Navigation web                   | Accès à un site web (ex: google.com)     | `curl -I https://google.com`             | Code HTTP 200                      | ✔                   | 🟢 OK      |
| T06         | Règles NAT actives                | Vérification des règles iptables         | `sudo iptables -t nat -L`                 | Règle MASQUERADE présente          | ✔                   | 🟢 OK      |

---
## 3. Tests de robustesse
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T07         | Redémarrage service               | Redémarrage de `hostapd` et `dnsmasq`   | `sudo systemctl restart hostapd dnsmasq`  | Services actifs, hotspot disponible | ✔                   | 🟢 OK      |
| T08         | Reboot RPi                        | Redémarrage complet du RPi               | `sudo reboot`                            | Hotspot disponible après reboot    | ✔                   | 🟢 OK      |
| T09         | Charge réseau                     | 5 clients connectés simultanément        | Connexion de 5 appareils                 | Hotspot stable, pas de déconnexion | ✔                   | 🟢 OK      |

---
## 4. Tests d’intégration
| **ID Test** | **Fonctionnalité**               | **Description**                          | **Méthode/Commande**                     | **Résultat attendu**               | **Résultat obtenu** | **Statut** |
|-------------|-----------------------------------|------------------------------------------|------------------------------------------|------------------------------------|---------------------|------------|
| T10         | Accès depuis RPi2 (NAS)           | RPi2 se connecte au hotspot              | `ping 192.168.4.1` depuis RPi2           | Réponse ICMP                       | ✔                   | 🟢 OK      |
| T11         | Accès depuis RPi3 (SGBD)          | RPi3 se connecte au hotspot              | `ping 8.8.8.8` depuis RPi3               | Accès Internet fonctionnel         | ✔                   | 🟢 OK      |

---
## 5. Observations et points d’amélioration
- **Succès** : Le hotspot est stable et le NAT fonctionne correctement.
- **Points à améliorer** :
  - Ajouter un script de monitoring pour surveiller la charge CPU lors de multiples connexions.
  - Documenter la procédure de changement du mot de passe Wi-Fi.

---
## 6. Validation globale
**Statut final** : 🟢 **Validé**
**Commentaires** : Tous les tests sont passés. Le service est prêt pour l’intégration avec les autres groupes.

---
