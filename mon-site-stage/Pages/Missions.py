import streamlit as st
from components.styles import inject_custom_css
from components.mission_tree import render_mission_tree
from components.data import MISSIONS

inject_custom_css()

st.title("🚀 Mes Missions chez FIS")
st.markdown("""
---
**Découvrez l’environnement technique sur lequel j’ai travaillé.**
Cliquez sur un élément de l’arborescence pour en savoir plus.
---
""")

# --- Layout ---
col_tree, col_info = st.columns([1, 2])

# --- Arborescence (colonne de gauche) ---
with col_tree:
    st.success("## 📦 deployment")
    st.markdown("Ce dossier représente l’environnement utilisé durant mon stage. Il regroupe les configurations, les scripts et les outils nécessaires au projet.")
    render_mission_tree()

# --- Contenu (colonne de droite) ---
with col_info:
    if "page" not in st.session_state:
        st.session_state.page = "Accueil"

    # --- Accueil des missions ---
    if st.session_state.page == "Accueil":
        st.header("Bienvenue dans mes missions !")
        st.markdown("""
        **Pourquoi cette arborescence ?**
        Derrière chaque application se cachent des **serveurs, des configurations, des scripts et des outils de déploiement**.
        Mon travail consistait à **automatiser et organiser** ces éléments pour rendre les déploiements **plus fiables et plus rapides**.

        **Comment explorer ?**
        Cliquez sur un dossier ou un fichier dans l’arborescence de gauche pour découvrir :
        - **Son rôle** dans le projet.
        - **Le processus** associé.
        - **Les scripts** que j’ai développés ou utilisés.
        - **Les résultats** obtenus.
        """)

    # --- Playbooks ---
    elif st.session_state.page == "playbooks":
        mission = MISSIONS["playbooks"]
        st.header(mission["title"])
        st.markdown(f"**{mission['description']}**")

        st.subheader("🔍 **Comprendre**")
        st.markdown("""
        Les playbooks sont des **scénarios écrits en YAML** qui décrivent les actions à exécuter sur les serveurs.
        **Exemple** : Le playbook `deploy_fisrelay.yml` permet de :
        - Vérifier que l’environnement est prêt.
        - Sauvegarder la configuration actuelle.
        - Installer la nouvelle version de FIS Relay.
        - Déployer les fichiers de configuration.
        - Redémarrer le service.
        """)

        st.subheader("📋 **Processus**")
        for step in mission["processus"]:
            st.markdown(f"- {step}")

        st.subheader("💻 **Scripts associés**")
        for script in mission["scripts"]:
            st.code(script, language="bash")

        st.subheader("✅ **Résultat**")
        st.success(mission["resultat"])

        st.markdown("---")
        st.markdown("**Extrait de playbook :**")
        st.code("""
        - name: Deploy FIS Relay
          hosts: fisrelay_servers
          tasks:
            - name: Backup current config
              copy:
                src: /path/to/current/config
                dest: /path/to/backup/
            - name: Install new version
              command: /path/to/install_script.sh
        """, language="yaml")

    # --- Inventories ---
    elif st.session_state.page == "inventories":
        mission = MISSIONS["inventories"]
        st.header(mission["title"])
        st.markdown(f"**{mission['description']}**")

        st.subheader("🔍 **Comprendre**")
        st.markdown("""
        Les inventories sont des **fichiers INI ou YAML** qui lient les serveurs aux configurations.
        **Exemple** :
        ```ini
        [production]
        server1.fis.com
        server2.fis.com

        [staging]
        test-server.fis.com
        ```
        """)

        st.subheader("📋 **Processus**")
        for step in mission["processus"]:
            st.markdown(f"- {step}")

        st.subheader("✅ **Résultat**")
        st.success(mission["resultat"])

    # --- FIS Relay ---
    elif st.session_state.page == "fisrelay":
        mission = MISSIONS["fisrelay"]
        st.header(mission["title"])
        st.markdown(f"**{mission['description']}**")

        st.subheader("🔍 **Comprendre**")
        st.markdown("""
        **Problématique** : Chaque serveur avait sa propre configuration, avec des **paramètres dupliqués** (ex: `Path = /relay`).
        Cela rendait la maintenance **longue et source d’erreurs**.

        **Solution** : J’ai travaillé sur une **réorganisation des fichiers** :
        - **Commons** : Fichiers avec les paramètres **partagés** par tous les serveurs.
        - **.sub** : Fichiers avec les paramètres **spécifiques** à chaque serveur.
        """)

        st.subheader("📋 **Processus**")
        for step in mission["processus"]:
            st.markdown(f"- {step}")

        st.subheader("💻 **Scripts associés**")
        for script in mission["scripts"]:
            st.code(script, language="bash")

        st.subheader("✅ **Résultat**")
        st.success(mission["resultat"])

        st.markdown("---")
        st.markdown("**Exemple de structure :**")
        st.code("""
        📁 fisrelay/
        ├── 📄 commons.ini          # Paramètres partagés (ex: Path = /relay)
        ├── 📁 environments/
        │   ├── 📄 prod.ini         # Paramètres spécifiques à la production
        │   └── 📄 staging.ini      # Paramètres spécifiques au staging
        └── 📁 sub/
            ├── 📄 server1.sub      # Paramètres uniques pour server1
            └── 📄 server2.sub      # Paramètres uniques pour server2
        """)

        st.markdown("**Avant/Après :**")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**❌ Avant (duplication)**")
            st.code("""
            # server1.ini
            ServerID = A01
            Path = /relay
            Port = 8000

            # server2.ini
            ServerID = B01
            Path = /relay  # Duplication !
            Port = 8000     # Duplication !
            """)
        with col2:
            st.markdown("**✅ Après (centralisé)**")
            st.code("""
            # commons.ini
            Path = /relay
            Port = 8000

            # server1.sub
            ServerID = A01

            # server2.sub
            ServerID = B01
            """)

    # --- Jenkins ---
    elif st.session_state.page == "jenkins":
        st.header("🚀 Jenkins")
        st.markdown("""
        **Jenkins** est un outil d’**automatisation des déploiements**.
        Une fois les configurations préparées, Jenkins lance les **playbooks Ansible** pour déployer automatiquement les applications sur les serveurs.

        ### 🔧 **Comment ça marche ?**
        1. **Préparation** : Les configurations sont générées via les scripts (commons, .sub).
        2. **Lancement** : Jenkins exécute le **Jenkinsfile** (pipeline de déploiement).
        3. **Déploiement** : Ansible prend le relais pour installer les configurations sur les serveurs.
        4. **Vérification** : Jenkins vérifie que tout s’est bien passé.

        ### 📄 **Jenkinsfile (exemple simplifié)**
        """)
        st.code("""
        pipeline {
            agent any
            stages {
                stage('Checkout') {
                    steps {
                        git 'https://github.com/fis/repo.git'
                    }
                }
                stage('Deploy') {
                    steps {
                        sh 'ansible-playbook deploy_fisrelay.yml -i inventory_prod.ini'
                    }
                }
            }
        }
        """, language="groovy")

        st.markdown("""
        ### ✅ **Avantages**
        - **Déploiements en 1 clic** : Plus besoin de tout faire manuellement.
        - **Traçabilité** : Jenkins garde un historique de tous les déploiements.
        - **Fiabilité** : Moins d’erreurs humaines.
        """)

    # --- Autres missions (à compléter) ---
    elif st.session_state.page in ["fisrelay_calendar", "fisrelay_enrichdata", "build_common", "restore_ini_fisrelay"]:
        st.header(f"📁 {st.session_state.page.replace('_', ' ').title()}")
        st.info("➡️ **Contenu à compléter** : Cette section sera détaillée prochainement.")
