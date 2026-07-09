import streamlit as st
from components.styles import inject_custom_css
from components.data import STAGE_INFO

inject_custom_css()

st.title("🌍 Projet Personnel : Stage Intensif d’Anglais")
st.markdown(f"""
---
## 📅 **Dates** : {STAGE_INFO['projet_personnel_dates']}
## 🎯 **Type** : Stage intensif d’anglais (à compléter)
---
""")

st.markdown("""
### 📝 **À compléter**
Cette section est réservée à mon projet personnel de **2 semaines** (13/07–24/07).
Je la remplirai une fois le stage terminé.
""")

# --- Zones à compléter ---
st.subheader("📌 **Objectifs**")
objectifs = st.text_area(
    "Décrivez les objectifs de ce projet (ex: améliorer mon anglais technique, passer un test, etc.)",
    height=100,
    placeholder="Exemple : Améliorer mon anglais pour travailler dans un environnement international..."
)

st.subheader("📌 **Réalisations**")
realisations = st.text_area(
    "Qu’avez-vous concrètement réalisé ?",
    height=100,
    placeholder="Exemple : Participation à des cours intensifs, passage du TOEIC, etc."
)

st.subheader("📌 **Difficultés**")
difficultes = st.text_area(
    "Quelles difficultés avez-vous rencontrées ?",
    height=100,
    placeholder="Exemple : Compréhension des termes techniques en anglais..."
)

st.subheader("📌 **Apports**")
apports = st.text_area(
    "Que retirez-vous de cette expérience ? (compétences, savoir-être, etc.)",
    height=100,
    placeholder="Exemple : Meilleure maîtrise de l'anglais, confiance en moi..."
)

st.subheader("📌 **Lien avec mon parcours TEMA**")
lien_parcours = st.text_area(
    "Comment ce projet s’inscrit-il dans votre parcours ?",
    height=100,
    placeholder="Exemple : Ouverture à l'international, préparation à un stage à l'étranger..."
)

st.markdown("---")
st.subheader("📄 **Justificatif**")
st.markdown("""
*(À déposer plus tard : certificat de stage, score au test d’anglais, etc.)*
""")
st.download_button(
    label="📥 Télécharger le justificatif (à ajouter)",
    data=None,
    file_name="justificatif_projet_personnel.pdf",
    disabled=True,
    help="Le PDF sera disponible une fois le projet terminé."
)
