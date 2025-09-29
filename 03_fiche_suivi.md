## **Fiche de suivi de projet par groupe (exemple)**

| Groupe   | Tâche principale                          | Statut       | Avancement (%) | Problèmes rencontrés   | Besoins d’aide ? | Prochaine étape                    | Responsable | Dernière mise à jour |
| -------- | ----------------------------------------- | ------------ | -------------- | ---------------------- | ---------------- | ---------------------------------- | ----------- | -------------------- |
| Groupe 1 | Mise en place du Hotspot Wi-Fi + NAT      | 🟡 En cours  | 60%            | NAT non fonctionnel    | Oui              | Vérifier règles `iptables`         | .....       | 30/09/2025           |
| Groupe 2 | Serveur NAS avec partages publics/privés  | 🟢 Terminé   | 100%           | Aucun                  | Non              | Finaliser documentation            | .....     | 30/09/2025           |
| Groupe 3 | SGBD (MariaDB) + gestion des accès/droits | 🔴 En retard | 30%            | MariaDB ne démarre pas | Oui              | Revoir `mysql_secure_installation` | .....         | 30/09/2025           |

---

### **Légende du champ "Statut"**

| Icône | Signification      |
| ----- | ------------------ |
| 🟢    | Terminé            |
| 🟡    | En cours           |
| 🔴    | En retard / bloqué |
| ⚪     | Non commencé       |

---

## **Feuille 2 : Suivi des livrables (exemple)**

| Groupe   | Script installé | Documentation technique | Fiche de recette | Présentation finale | Commentaires                   |
| -------- | --------------- | ----------------------- | ---------------- | ------------------- | ------------------------------ |
| Groupe 1 | ✅               | ✅                       | ⚠️ Incomplète    | 🕓 En préparation   | À compléter avant le jalon     |
| Groupe 2 | ✅               | ✅                       | ✅                | ✅                   | -                              |
| Groupe 3 | ⚠️ Partiel      | ⚠️ En cours             | ❌                | 🕓 Prévue           | Avancer sur la base de données |

---

## **Feuille 3 : Planification / Jalons (exemple)**

| Date       | Objectif / Jalon                                 | Livrables attendus                           | Statut |
| ---------- | ------------------------------------------------ | -------------------------------------------- | ------ |
| 30/09/2025 | Jalon intermédiaire – Réseau Wi-Fi opérationnel  | RPi1 en mode hotspot avec DHCP               | 🟡     |
| 30/09/2025 | Jalon intermédiaire – NAS monté depuis un client | Partages public/privé testés et fonctionnels | 🟢     |
| 30/09/2025 | Finalisation du SGBD                             | Base publique + accès admin opérationnels    | 🔴     |
| 01/10/2025 | Livraison finale                                 | Tous les livrables remis                     | ⚪      |

---

### **Légende du champ "Statut"**

| Icône | Signification      |
| ----- | ------------------ |
| 🟢    | Terminé            |
| 🟡    | En cours           |
| 🔴    | En retard / bloqué |
| ⚪     | Non commencé       |
