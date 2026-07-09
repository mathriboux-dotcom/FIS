import streamlit as st
from components.styles import inject_custom_css
from components.data import STAGE_INFO

# --- CONFIG ---
st.set_page_config(
    page_title="Stage FIS - Mathilde Riboux",
    page_icon="💻",
    layout="wide"
)

# --- CSS ---
inject_custom_css()

# --- CONNEXION ---
PASSWORD = "070809"
if "connected" not in st.session_state:
    st.session_state.connected = False

if not st.session_state.connected:
    st.title("🔒 Accès sécurisé")
    st.markdown(f"""
    Bienvenue sur mon site de retour d'expérience de stage chez **{STAGE_INFO['entreprise']}**.
    Pour accéder au contenu, veuillez saisir le mot de passe.
    """)
    pwd = st.text_input("Mot de passe", type="password")
    if st.button("Entrer"):
        if pwd == PASSWORD:
            st.session_state.connected = True
            st.rerun()
        else:
            st.error("❌ Mot de passe incorrect.")
    st.stop()

# --- ACCUEIL ---
st.title("💻 Mon Stage chez FIS Financial Systems France")
st.markdown(f"""
## {STAGE_INFO['duree']} | Tuteur : {STAGE_INFO['tuteur']} | {STAGE_INFO['dates']}
---
**Découvrez mon parcours, mes missions et ce que j’ai appris pendant ce stage.**
""")

st.markdown("""
### 📌 Navigation
- [Qui suis-je ?](/02_Qui_suis_je)
- [Mon stage chez FIS](/03_Mon_stage)
- [🚀 Mes missions (Arborescence interactive)](/04_Missions)
- [Projet personnel (Anglais)](/05_Projet_personnel)
- [Ce que j’ai appris](/06_Ce_que_jai_appris)
- [Mon bilan](/07_Mon_bilan)
- [Annexes (PDFs)](/08_Annexes)
""")
