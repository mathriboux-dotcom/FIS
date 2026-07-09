import streamlit as st
from components.styles import inject_custom_css

inject_custom_css()

st.title("🎓 Ce que j’ai appris")
st.markdown("""
---
## 🧠 **Compétences et Savoirs**
Ce stage m’a permis de développer des **compétences techniques et transversales**, mais aussi de mieux comprendre **le monde de l’entreprise et la transformation digitale**.
---
""")

st.subheader("🔧 **Compétences Techniques**")
st.markdown("""
### **Outils découverts**
| Outil       | Rôle                                                                 | Ce que j’ai appris                                                                 |
|-------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Ansible** | Automatisation des déploiements                                    | Créer des playbooks, gérer des inventories, déployer des configurations.          |
| **Jenkins** | Orchestration des déploiements                                     | Configurer des pipelines, lancer des jobs, suivre les déploiements.               |
| **Linux**   | Système d’exploitation des serveurs                                | Naviguer dans les répertoires, exécuter des commandes, gérer des fichiers.        |
| **Git**     | Gestion de versions                                                  | Cloner un dépôt, consulter l’historique, comprendre les branches.                 |
| **Jira**    | Suivi des tâches                                                     | Créer des tickets, suivre l’avancement, collaborer avec l’équipe.                 |

### **Scripts Bash**
J’ai développé et maintenu plusieurs scripts pour :
- **Automatiser la génération des configurations** (ex: `build_all_common_ini_prod.sh`).
- **Comparer des fichiers** (ex: `compare_common_staging_vs_production.sh`).
- **Reconstruire des configurations** (ex: `restore_ini_fisrelay.sh`).

**Exemple de script :**
""")
st.code("""
#!/bin/bash
# build_all_common_ini_prod.sh
# Objectif : Générer les fichiers commons pour la production

# 1. Récupérer les configurations de tous les serveurs
scp user@server1:/path/to/config.ini ./temp/
scp user@server2:/path/to/config.ini ./temp/

# 2. Extraire les paramètres communs
grep -F -f common_params.txt ./temp/*.ini > commons.ini

# 3. Nettoyer les fichiers temporaires
rm -rf ./temp/
""", language="bash")

st.subheader("📈 **Transformation Digitale**")
st.markdown("""
Chez FIS, j’ai pu observer **concrètement** comment la transformation digitale impacte le secteur financier :
- **Automatisation** : Remplacement des tâches manuelles par des scripts (ex: génération des configurations).
- **Fiabilité** : Réduction des erreurs humaines grâce à des processus standardisés.
- **Rapidité** : Déploiements en quelques minutes au lieu de plusieurs heures.
- **Collaboration** : Utilisation d’outils comme **Jenkins** et **Ansible** pour orchestrer le travail d’équipe.

**Exemple concret** :
Avant mon stage, les configurations étaient modifiées **manuellement** sur chaque serveur → **risque d’erreurs élevé**.
Avec les scripts que j’ai développés, les configurations sont **générées automatiquement** et déployées via Ansible → **zéro erreur de duplication**.
""")

st.subheader("💡 **Savoir-Être et Savoir-Faire**")
st.markdown("""
### **Ce que j’ai développé**
| Compétence          | Exemple                                                                 |
|---------------------|-------------------------------------------------------------------------|
| **Analyse**         | Comprendre un problème avant de chercher une solution.                 |
| **Autonomie**       | Apprendre à utiliser de nouveaux outils (Linux, Ansible) en peu de temps. |
| **Rigueur**         | Vérifier systématiquement mes scripts avant de les exécuter.          |
| **Communication**   | Expliquer mon travail à mon tuteur ou à l’équipe.                     |
| **Adaptabilité**    | M’adapter à un environnement technique complexe.                     |
| **Esprit d’équipe**  | Collaborer avec les autres stagiaires et les membres de l’équipe.    |

### **Mon recul sur le monde professionnel**
- **L’importance de la collaboration** : Un projet ne repose pas sur une seule personne, mais sur une **équipe soudée**.
- **La valeur de l’automatisation** : Dans un monde où la complexité augmente, **automatiser = gagner du temps et réduire les erreurs**.
- **La nécessité de la documentation** : Un bon code ou un bon processus doit être **compréhensible par les autres**.
""")
