import streamlit as st
from components.styles import inject_custom_css
from components.data import STAGE_INFO

inject_custom_css()

st.title("💻 Mon Stage chez FIS Financial Systems France")
st.markdown(f"""
## 📅 {STAGE_INFO['duree']} | 👤 Tuteur : {STAGE_INFO['tuteur']} | 🗓️ {STAGE_INFO['dates']}
---
**Bienvenue sur mon site de retour d'expérience !**
""")

st.markdown("""
### 🎯 **Pourquoi ce site ?**
Ce site a pour but de vous faire découvrir **mon stage chez FIS** de manière interactive et visuelle.
Je ne me contente pas de décrire mes missions : je vous montre **comment tout s’articule**, des scripts aux déploiements, en passant par les outils comme Ansible et Jenkins.

### 📖 **Comment naviguer ?**
- **Explorez l’arborescence** dans la section [Mes missions](04_Missions) pour comprendre mon travail au quotidien.
- **Découvrez mon parcours** et ce que j’ai appris dans les autres sections.
- **Téléchargez les justificatifs** dans les [Annexes](08_Annexes).

---
### 🔗 **Navigation rapide**
""")

st.markdown(f"""
- **[Qui suis-je ?](02_Qui_suis_je)** : Mon parcours à NEOMA et mes motivations.
- **[Mon stage chez FIS](03_Mon_stage)** : L’entreprise, mon équipe, mon arrivée.
- **[🚀 Mes missions](04_Missions)** : **Le cœur du site** – Arborescence interactive et détails techniques.
- **[Projet personnel (Anglais)](05_Projet_personnel)** : Stage intensif du {STAGE_INFO['projet_personnel_dates']}.
- **[Ce que j’ai appris](06_Ce_que_jai_appris)** : Compétences, transformation digitale, et recul.
- **[Mon bilan](07_Mon_bilan)** : Difficultés, évolution, et projet professionnel.
- **[Annexes](08_Annexes)** : Justificatifs et documents officiels.
""")
