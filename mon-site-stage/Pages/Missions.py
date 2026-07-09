import streamlit as st
from components.mission_tree import render_mission_tree
from components.styles import inject_custom_css

inject_custom_css()

st.title("🚀 Mes Missions chez FIS")
st.markdown("""
---
**Découvrez l'environnement technique sur lequel j'ai travaillé.**
Cliquez sur un élément de l'arborescence pour en savoir plus.
""")

# --- ARBORESCENCE (à gauche) ---
col_tree, col_info = st.columns([1, 2])

with col_tree:
    st.success("## 📦 deployment")
    render_mission_tree()  # Fonction définie dans components/mission_tree.py

# --- CONTENU (à droite) ---
with col_info:
    if "page" not in st.session_state:
        st.session_state.page = "Accueil"

    if st.session_state.page == "fisrelay":
        st.header("📁 FIS Relay")
        st.markdown("""
        ### 🔍 **Comprendre**
        Ce rôle gère les configurations de l'application **FIS Relay**, utilisée pour le routage des transactions financières.
        **Problématique** : Chaque serveur avait sa propre configuration, avec des paramètres dupliqués → risque d'erreurs et maintenance complexe.

        ### 📋 **Processus**
        1. **Analyse** : Identification des paramètres communs (ex: `Path = /relay`).
        2. **Centralisation** : Création de fichiers **commons** (valeurs partagées).
        3. **Personnalisation** : Génération de fichiers **.sub** (valeurs spécifiques par serveur).
        4. **Intégration** : Utilisation dans Ansible pour déployer automatiquement.

        ### 💻 **Scripts associés**
        - `build_all_common_ini_prod.sh` : Génère les commons pour la production.
        - `build_all_sub_fisrelay.sh` : Génère les fichiers .sub.
        - `restore_ini_fisrelay.sh` : Reconstruit la config finale pour vérification.

        ### ✅ **Résultat**
        - **Réduction des erreurs** : Moins de duplications → moins de risques de incohérences.
        - **Gain de temps** : Déploiement automatisé en 1 clic via Jenkins.
        - **Maintenabilité** : Une modification dans les commons est répercutée partout.
        """)
        st.image("assets/images/fisrelay_arborescence.png", caption="Arborescence du rôle FIS Relay")

    elif st.session_state.page == "playbooks":
        st.header("📁 Playbooks Ansible")
        st.markdown("""
        ### 🎯 **Rôle**
        Les playbooks définissent les étapes de déploiement (ex: installation, configuration, vérification).
        **Exemple** : Le playbook `deploy_fisrelay.yml` :
        - Vérifie l'environnement.
        - Sauvegarde l'ancienne version.
        - Installe la nouvelle version.
        - Déploie les configurations (commons + .sub).
        - Redémarre le service.

        ### 📄 **Extrait de code**
        ```yaml
        - name: Deploy FIS Relay
          hosts: fisrelay_servers
          tasks:
            - name: Backup current config
              copy:
                src: /path/to/current/config
                dest: /path/to/backup/
            - name: Install new version
              command: /path/to/install_script.sh
        ```
        """)

    # ... (autres pages : inventories, jenkins, etc.)
