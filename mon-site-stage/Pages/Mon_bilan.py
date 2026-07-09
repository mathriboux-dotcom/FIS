import streamlit as st
from components.styles import inject_custom_css

inject_custom_css()

st.title("✅ Mon Bilan")
st.markdown("""
---
## 📉 **Difficultés Rencontrées**
Au début du stage, j’ai dû faire face à plusieurs défis :
---
""")

st.subheader("🔹 **Comprendre l’environnement technique**")
st.markdown("""
- **Problème** : Je ne connaissais **ni Ansible, ni Jenkins, ni Linux** avant mon arrivée.
- **Solution** : J’ai passé du temps à **lire la documentation**, poser des questions à mon tuteur, et **expérimenter** sur des environnements de test.
- **Résultat** : Au bout de 2 semaines, je comprenais les bases et pouvais **contribuer activement** aux projets.
""")

st.subheader("🔹 **L’organisation des configurations**")
st.markdown("""
- **Problème** : Les configurations étaient **réparties sur des dizaines de fichiers**, avec des duplications et des incohérences.
- **Solution** : J’ai travaillé sur une **réorganisation** (commons + .sub) pour centraliser les paramètres.
- **Résultat** : Les déploiements sont devenus **plus simples et plus fiables**.
""")

st.subheader("🔹 **La lecture des scripts existants**")
st.markdown("""
- **Problème** : Les scripts étaient **complexes** et mal documentés.
- **Solution** : J’ai **décortiqué** chaque script, ajouté des commentaires, et demandé des explications à l’équipe.
- **Résultat** : J’ai pu **améliorer** certains scripts et en créer de nouveaux.
""")

st.markdown("---")
st.subheader("🌱 **Une Expérience qui m’a fait évoluer**")
st.markdown("""
Ce stage a été **bien plus qu’une expérience technique** :
- **Sur le plan professionnel** :
  - J’ai découvert **le monde de l’entreprise** et ses enjeux (fiabilité, collaboration, automatisation).
  - J’ai appris à **travailler en équipe** et à **communiquer clairement**.
  - J’ai développé une **rigueur** que je n’avais pas avant.

- **Sur le plan personnel** :
  - J’ai gagné en **confiance en moi** : je me sens capable d’apprendre de nouveaux outils rapidement.
  - J’ai appris à **poser des questions** sans hésiter.
  - J’ai compris que **les erreurs font partie de l’apprentissage**.

**Ce qui m’a particulièrement plu** :
✅ **La résolution de problèmes** : Trouver des solutions à des défis techniques.
✅ **L’automatisation** : Voir comment un script peut remplacer des heures de travail manuel.
✅ **L’ambiance d’équipe** : Travailler avec des collègues motivés et bienveillants.
""")

st.markdown("---")
st.subheader("🔮 **Une Réflexion sur mon Avenir Professionnel**")
st.markdown("""
Ce stage m’a ouvert les yeux sur **la diversité des métiers dans le numérique** :
- **DevOps** : Un domaine qui me plaît particulièrement, car il allie **technique et organisation**.
- **Consulting** : Aider les entreprises à **optimiser leurs processus** (comme j’ai fait avec les configurations).
- **Gestion de projet** : Coordonner des équipes et des outils pour **atteindre un objectif commun**.

**Mon projet pour la suite** :
- **Approfondir mes connaissances** en automatisation et en cloud (AWS, Azure).
- **Rechercher un stage ou une alternance** dans le DevOps ou le consulting IT.
- **Continuer à développer mon anglais** pour travailler dans un environnement international.

**En résumé** :
Ce stage a confirmé mon **intérêt pour les métiers à l’intersection de la technique et du management**, où je peux **résoudre des problèmes concrets** tout en **collaborant avec une équipe**.
""")
