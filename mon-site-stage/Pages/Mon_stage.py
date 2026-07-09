import streamlit as st
from components.styles import inject_custom_css
from components.data import STAGE_INFO

inject_custom_css()

st.title("🏢 Mon Stage chez FIS Financial Systems France")
st.markdown(f"""
---
## 📅 **Informations clés**
- **Entreprise** : {STAGE_INFO['entreprise']}
- **Dates** : {STAGE_INFO['dates']}
- **Durée** : {STAGE_INFO['duree']}
- **Tuteur** : {STAGE_INFO['tuteur']}
""")

st.markdown("""
---
## 🏗️ **Présentation de FIS**
**FIS (Fidelity National Information Services)** est un leader mondial dans les **technologies financières**.
L’entreprise propose des solutions logicielles et des services pour les **banques, les institutions financières et les entreprises**.

### 🎯 **Le secteur d’activité**
FIS opère dans un domaine où **la fiabilité et la sécurité sont primordiales** :
- Une erreur de configuration peut avoir des **conséquences financières importantes**.
- Les applications doivent être **déployées rapidement et sans interruption**.
- L’**automatisation** est donc au cœur des processus pour garantir **efficacité et cohérence**.

### 👥 **Mon équipe**
J’ai intégré une équipe dédiée à **l’automatisation des déploiements** et à la **gestion des configurations**.
Mon rôle consistait à :
- **Analyser les configurations existantes** (fichiers INI, scripts).
- **Automatiser la génération des fichiers** (commons, .sub).
- **Intégrer ces configurations dans Ansible** pour des déploiements fiables.

---
## 🚪 **Mon arrivée chez FIS**
### **Premier jour**
Dès mon arrivée, j’ai été accueillie avec :
- Un **ordinateur professionnel** et les accès nécessaires.
- Un **casque** pour les réunions.
- Un **badge** pour accéder aux locaux.

L’ambiance était **très accueillante** : les collègues prenaient le temps de répondre à mes questions, et j’ai rapidement trouvé mes repères.

### **Intégration**
- **Réunions quotidiennes** : Chaque après-midi, une réunion était organisée pour faire le point sur l’avancement des tâches.
- **Collaboration** : J’ai travaillé en binôme avec un autre stagiaire, ce qui a facilité l’apprentissage.
- **Outils** : J’ai découvert **Teams** (pour la communication), **Jira** (pour le suivi des tâches), et **Git** (pour la gestion du code).

---
## 💬 **Ce que j’ai retenu de l’entreprise**
- **Une culture de la collaboration** : Les équipes travaillent ensemble pour résoudre les problèmes.
- **L’importance de l’automatisation** : Dans un environnement complexe, chaque tâche répétitive doit être automatisée.
- **La rigueur** : Dans le secteur financier, une petite erreur peut avoir de grandes conséquences.
""")
