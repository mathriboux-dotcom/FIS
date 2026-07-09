import streamlit as st
from components.styles import inject_custom_css

inject_custom_css()

st.title("📎 Annexes")
st.markdown("""
---
## 📄 **Justificatifs et Documents**
Retrouvez ici les documents officiels liés à mon stage et à mon projet personnel.
---
""")

st.subheader("📄 **Convention de Stage**")
st.markdown("""
*(À déposer : convention de stage signée par NEOMA et FIS)*
""")
st.download_button(
    label="📥 Télécharger la convention de stage",
    data=None,
    file_name="convention_stage.pdf",
    disabled=True,
    help="La convention sera disponible une fois signée."
)

st.markdown("---")
st.subheader("💰 **Reçu / Acte de Paiement**")
st.markdown("""
*(À déposer : reçu de paiement ou attestation de stage)*
""")
st.download_button(
    label="📥 Télécharger le reçu",
    data=None,
    file_name="recu_paiement.pdf",
    disabled=True,
    help="Le reçu sera disponible une fois le stage terminé."
)

st.markdown("---")
st.subheader("🌍 **Justificatif Projet Personnel (Anglais)**")
st.markdown("""
*(À déposer : certificat de stage, score au test d’anglais, etc.)*
""")
st.download_button(
    label="📥 Télécharger le justificatif",
    data=None,
    file_name="justificatif_projet_personnel.pdf",
    disabled=True,
    help="Le justificatif sera disponible une fois le projet terminé."
)

st.markdown("---")
st.subheader("🔗 **Liens Utiles**")
st.markdown("""
- [Site de FIS Financial Systems France](https://www.fisglobal.com/fr-fr)
- [Site de NEOMA Business School](https://www.neoma-bs.fr/)
- [Documentation Ansible](https://docs.ansible.com/)
- [Documentation Jenkins](https://www.jenkins.io/doc/)
""")
