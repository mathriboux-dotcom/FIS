import streamlit as st
from components.styles import inject_custom_css
from components.data import *

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
    st.markdown("""
    <div class="login-container">
        <h1>🔒 Accès sécurisé</h1>
        <p>Bienvenue sur mon site de retour d'expérience de stage chez <strong>FIS Financial Systems France</strong>.</p>
        <p>Pour accéder au contenu, veuillez saisir le mot de passe.</p>
    </div>
    """, unsafe_allow_html=True)
    pwd = st.text_input("Mot de passe", type="password", key="pwd_input")
    if st.button("Entrer", key="login_button"):
        if pwd == PASSWORD:
            st.session_state.connected = True
            st.rerun()
        else:
            st.error("❌ Mot de passe incorrect.")
    st.stop()

# --- INITIALISATION DES ÉTATS ---
if "page" not in st.session_state:
    st.session_state.page = "Accueil"
if "sub_page" not in st.session_state:
    st.session_state.sub_page = None

# --- SIDEBAR (Navigation principale) ---
with st.sidebar:
    st.markdown("""
    <div class="sidebar-title">
        <h2>📚 Navigation</h2>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Aller à :",
        [
            "🏠 Accueil",
            "👤 Qui suis-je ?",
            "🏢 Mon stage chez FIS",
            "🚀 Mes missions",
            "🎓 Ce que j’ai appris",
            "📊 Mon bilan",
            "📎 Annexes"
        ],
        key="main_page",
        label_visibility="collapsed"
    )
    st.session_state.page = page

    # Réinitialiser la sous-page à chaque changement de page principale
    if st.session_state.page != st.session_state.get("last_page", None):
        st.session_state.sub_page = None
        st.session_state.last_page = st.session_state.page

# --- CONTENU PRINCIPAL ---
def render_page():
    if st.session_state.page == "🏠 Accueil":
        render_accueil()
    elif st.session_state.page == "👤 Qui suis-je ?":
        render_qui_suis_je()
    elif st.session_state.page == "🏢 Mon stage chez FIS":
        render_mon_stage()
    elif st.session_state.page == "🚀 Mes missions":
        render_missions()
    elif st.session_state.page == "🎓 Ce que j’ai appris":
        render_ce_que_jai_appris()
    elif st.session_state.page == "📊 Mon bilan":
        render_mon_bilan()
    elif st.session_state.page == "📎 Annexes":
        render_annexes()

render_page()

# --- FONCTIONS DE RENDU DES PAGES ---
def render_accueil():
    st.title("💻 Mon Stage chez FIS Financial Systems France")
    st.markdown("""
    <div class="hero-section">
        <p class="hero-text">
            Bienvenue sur mon site de retour d'expérience de stage.
            <br><br>
            Au cours de ma première année à <strong>TEMA (NEOMA Business School)</strong>, j'ai effectué un stage chez
            <strong>FIS Financial Systems France</strong>. Cette expérience m'a permis de découvrir le fonctionnement d'une entreprise
            spécialisée dans les <strong>technologies financières</strong>.
            <br><br>
            J'ai intégré une équipe travaillant sur <strong>l'automatisation des déploiements</strong> et l'organisation des configurations
            utilisées par les applications. Tout au long de ce stage, j'ai découvert de nouveaux outils, participé à plusieurs projets et
            développé de nouvelles compétences.
            <br><br>
            À travers ce site, je vous propose de découvrir :
        </p>
        <ul class="hero-list">
            <li>🏢 L'entreprise <strong>FIS</strong> ;</li>
            <li>📂 Les <strong>missions</strong> que j'ai réalisées ;</li>
            <li>🛠️ Les <strong>outils</strong> que j'ai découverts ;</li>
            <li>🧠 Les <strong>compétences</strong> que j'ai développées ;</li>
            <li>📊 Le <strong>bilan</strong> que je retire de cette expérience.</li>
        </ul>
        <p class="hero-closing">Bonne visite ! 😊</p>
    </div>
    """, unsafe_allow_html=True)

def render_qui_suis_je():
    st.title("👤 Qui suis-je ?")
    st.markdown("""
    <div class="section">
        <h2>📸 Bannière d'introduction</h2>
        <p>
            <em>Idée d'image :</em> Photo de moi dans un environnement professionnel, ou sur le campus de NEOMA,
            ou devant un ordinateur.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Une formation tournée vers plusieurs domaines")
    st.markdown("""
    Je m’appelle **Mathilde Riboux** et je suis étudiante en première année du programme **TEMA** à **NEOMA Business School**.
    TEMA est une formation qui associe le **management**, le **commerce** et le **numérique**.
    Depuis le début de l’année, j’ai découvert des domaines très variés. J’ai étudié aussi bien l’entreprise que les technologies.
    Cette diversité m’a permis d’acquérir une première vision du monde professionnel.
    Cependant, une question revenait souvent : <em>Je comprenais les notions vues en cours, mais je voyais difficilement comment elles étaient utilisées dans une entreprise.</em>
    """)

    st.markdown("---")
    st.subheader("Pourquoi ce stage ?")
    st.markdown("""
    C’est cette curiosité qui m’a donné envie d’effectuer mon stage chez **FIS Financial Systems France**.
    Je souhaitais découvrir un **environnement professionnel concret**. Je voulais surtout comprendre ce qu’il se passe derrière les outils numériques
    utilisés chaque jour par les entreprises.
    <br><br>
    Ce stage représentait également une occasion d’explorer un secteur que je ne connaissais pas encore. Je cherchais à mieux comprendre
    les métiers qui composent ce domaine et les possibilités qu’il pouvait offrir.
    """)

    st.markdown("---")
    st.subheader("Une découverte d’un nouveau domaine")
    st.markdown("""
    Avant ce stage, je connaissais surtout l’informatique à travers les cours. Je n’avais jamais travaillé avec des serveurs ou des outils de déploiement.
    Je ne connaissais pas encore le **DevOps**, un domaine qui facilite l’installation et la gestion des applications grâce à l’automatisation.
    <br><br>
    Mon arrivée chez FIS a donc marqué le début d’une **véritable découverte**. Au fil des semaines, j’ai compris qu’une application ne repose pas
    uniquement sur son interface. Derrière son fonctionnement se cachent de nombreux outils, fichiers et configurations. Tous ces éléments doivent
    fonctionner ensemble pour garantir son bon fonctionnement. Cette réalité m’était totalement inconnue avant mon arrivée.
    """)

def render_mon_stage():
    st.title("🏢 Mon stage chez FIS")

    # Sous-menu pour les sections de "Mon stage"
    sub_page = st.selectbox(
        "Explorer :",
        [
            "Mon arrivée chez FIS",
            "Découverte de FIS",
            "Une entreprise composée de nombreux métiers",
            "Un environnement enrichissant",
            "Mon équipe"
        ],
        key="mon_stage_subpage"
    )

    if sub_page == "Mon arrivée chez FIS":
        st.markdown("""
        Mon premier jour chez FIS a marqué le début de cette nouvelle expérience.
        Dès mon arrivée, j’ai reçu le matériel nécessaire pour travailler dans de bonnes conditions :
        un ordinateur professionnel, un casque et un badge d’accès. J’ai également obtenu les différents accès nécessaires pour commencer mes missions.
        <br><br>
        Très rapidement, j’ai découvert une **ambiance de travail agréable et accueillante**. Les échanges entre collègues étaient nombreux et chacun
        prenait facilement le temps de répondre à mes questions. Cette atmosphère m’a permis de trouver rapidement mes repères.
        <br><br>
        J’ai également participé à différents moments de convivialité. Au cours de mon stage, j’ai notamment pris part à un dîner d’équipe ainsi qu’à
        une crêpe party organisée dans l’entreprise. Ces événements facilitaient les échanges entre les collaborateurs. Ils permettaient aussi de découvrir
        l’entreprise sous un autre angle.
        """)

    elif sub_page == "Découverte de FIS":
        st.markdown("""
        Avant ce stage, je connaissais peu le secteur des **technologies financières**.
        J’ai découvert une entreprise spécialisée dans le développement de solutions destinées au monde de la finance.
        Les technologies développées par FIS sont utilisées par différents acteurs du secteur financier.
        <br><br>
        Cette activité repose sur des outils performants mais aussi sur la **collaboration de nombreuses équipes**. Au fil des semaines, j’ai compris que
        la technologie est au cœur du fonctionnement de l’entreprise.
        <br><br>
        J’ai également découvert l’importance de la **fiabilité** dans ce domaine. Dans le secteur financier, une erreur de configuration ou une interruption
        de service peut avoir des conséquences importantes. Les applications doivent donc fonctionner de manière continue et être déployées avec le plus
        de sécurité possible.
        <br><br>
        J’ai également compris pourquoi **l’automatisation** occupe aujourd’hui une place essentielle. Les infrastructures deviennent de plus en plus complexes
        et les équipes doivent gérer un grand nombre de serveurs et de configurations. L’automatisation permet de réduire les erreurs humaines, de gagner du
        temps et de garantir que chaque opération est réalisée de façon cohérente.
        <br><br>
        C’est précisément cette logique que j’ai retrouvée dans les projets sur lesquels j’ai travaillé durant mon stage. Les missions qui m’ont été confiées
        avaient toutes pour objectif de **simplifier la gestion des configurations** et de rendre les déploiements plus fiables.
        """)

    elif sub_page == "Une entreprise composée de nombreux métiers":
        st.markdown("""
        L’un des éléments qui m’a le plus marquée est la **diversité des profils** présents dans l’entreprise.
        Avant mon stage, j’imaginais surtout les métiers techniques. La réalité est beaucoup plus riche.
        <br><br>
        Développeurs, équipes de production, commerciaux, ressources humaines et de nombreux autres services collaborent au quotidien.
        Chacun apporte ses compétences à la réalisation des projets.
        <br><br>
        Cette organisation m’a permis de mieux comprendre le **fonctionnement global de l’entreprise**. J’ai découvert qu’un projet ne repose jamais sur
        une seule équipe. La réussite d’un projet dépend de la **collaboration entre plusieurs métiers**.
        """)

    elif sub_page == "Un environnement enrichissant":
        st.markdown("""
        Au-delà de mes missions, j’ai apprécié les échanges avec les collaborateurs.
        Les discussions ne portaient pas uniquement sur les projets en cours. Lors des pauses ou des repas, les sujets abordés étaient souvent très variés.
        <br><br>
        Les conversations pouvaient par exemple concerner l’actualité économique ou les évolutions du secteur financier.
        Ces échanges m’ont permis de découvrir de nouveaux sujets et de mieux comprendre l’environnement dans lequel évolue l’entreprise.
        <br><br>
        Petit à petit, j’ai développé une **vision plus large** de ce secteur d’activité.
        """)

    elif sub_page == "Mon équipe":
        st.markdown("""
        Durant ce stage, j’ai intégré une équipe travaillant sur les **déploiements et la gestion des configurations**.
        Une grande partie de mon travail se faisait aux côtés d’un autre stagiaire. Nous travaillions souvent sur des sujets similaires et nous nous entraidions régulièrement.
        <br><br>
        Lorsque l’un de nous trouvait une solution à un problème, cela permettait souvent d’aider l’autre à avancer plus rapidement.
        Cette collaboration a rendu certaines difficultés plus faciles à surmonter.
        <br><br>
        Les échanges ne se faisaient pas uniquement en présentiel. Une partie importante de la communication passait également par **Teams**, un outil utilisé pour
        échanger des messages, partager des informations et organiser des réunions.
        <br><br>
        Chaque après-midi, une réunion était organisée autour du projet sur lequel nous travaillions. Cette réunion permettait de faire le point sur l’avancement
        des tâches et d’échanger sur les éventuelles difficultés rencontrées.
        <br><br>
        Plusieurs personnes y participaient régulièrement, notamment mon maître de stage, un membre de l’équipe de développement ainsi que des collaborateurs
        travaillant autour de la production.
        <br><br>
        Ces échanges m’ont permis de mieux comprendre les **objectifs du projet** et le rôle de chacun.
        J’ai également découvert l’importance de la **communication** dans un environnement professionnel.
        Même lorsque les équipes travaillent sur des sujets différents, elles doivent rester en contact afin d’avancer dans la même direction.
        <br><br>
        Cette organisation m’a montré qu’un projet repose autant sur la **collaboration entre les personnes** que sur les outils utilisés.
        """)

def render_missions():
    st.title("🚀 Mes Missions")

    # Menu pour les sous-sections des missions
    mission_sub_page = st.selectbox(
        "Sélectionnez une mission :",
        [
            "📁 Playbooks",
            "📁 Inventories",
            "📁 FIS Relay",
            "📅 FIS Relay Calendar",
            "📊 FIS Relay EnrichData",
            "⚖️ FIS Relay Load Balancing",
            "🔀 FIS Relay Session Chooser",
            "📁 Scripts build_common",
            "📁 Scripts build_sub_ini_ansible",
            "📄 restore_ini_fisrelay.sh",
            "🚀 Jenkins"
        ],
        key="missions_subpage"
    )

    if mission_sub_page == "📁 Playbooks":
        st.markdown("""
        ### 📌 À quoi servent les playbooks ?
        Les playbooks pilotent les différentes étapes du déploiement. Ils permettent d’organiser les actions à réaliser dans un ordre précis afin de garantir
        une installation cohérente sur tous les serveurs. Durant mon stage, j’ai développé le playbook principal utilisé pour le déploiement de **FIS Relay**.
        <br><br>
        ### 🔍 Logique générale
        1. **Vérification de l’environnement** : Contrôle des paramètres, des fichiers et des configurations nécessaires au déploiement.
        2. **Préparation du serveur** : Création des dossiers et préparation des éléments nécessaires à l’installation.
        3. **Sauvegarde de l’installation existante** : Conservation de la version précédente afin de pouvoir revenir en arrière en cas de problème.
        4. **Installation de la nouvelle version** : Déploiement et installation automatique de l’application.
        5. **Déploiement des configurations** : Mise en place des fichiers de configuration nécessaires au fonctionnement de FIS Relay.
        6. **Vérification** : Contrôle du bon déroulement du déploiement.
        7. **Démarrage du service** : Lancement de l’application et vérification de son bon fonctionnement.
        <br><br>
        ### 💻 Exemple réel
        *(Capture d’écran du playbook ici – à ajouter dans `assets/images/playbook.png`)*
        <br><br>
        **Figure 1** : Extrait du playbook FIS Relay développé durant mon stage.
        <br><br>
        ### 🚀 Projet réalisé
        Dans le cadre de mon stage, j’ai conçu et développé le playbook principal de déploiement de FIS Relay.
        Ce playbook centralise l’ensemble du processus de déploiement :
        - Préparation de l’environnement ;
        - Création des sauvegardes ;
        - Installation de l’application ;
        - Déploiement des configurations ;
        - Contrôles de sécurité ;
        - Vérifications finales du service.
        <br><br>
        L’objectif était de rendre les déploiements **plus fiables, plus rapides et moins dépendants des manipulations manuelles**.
        """)

    elif mission_sub_page == "📁 Inventories":
        st.markdown("""
        ### 📌 À quoi servent les inventories ?
        Les inventories regroupent les informations permettant d’identifier les serveurs utilisés lors des déploiements.
        Ils indiquent notamment quelles machines sont concernées par une opération et permettent aux playbooks de savoir où exécuter les différentes actions prévues.
        Dans un environnement comportant plusieurs serveurs, ils facilitent l’organisation et la gestion des déploiements.
        <br><br>
        ### 🔍 Rôle dans le déploiement
        Les inventories constituent un lien entre les serveurs et les playbooks. Ils permettent :
        - D’identifier les machines concernées ;
        - De regrouper les serveurs par environnement ;
        - D’associer les paramètres nécessaires au déploiement ;
        - D’assurer l’exécution des opérations sur les bonnes machines.
        <br><br>
        Grâce à cette organisation, un même playbook peut être utilisé sur différents environnements tout en conservant des configurations adaptées.
        <br><br>
        ### 💻 Exemple simplifié
        ```ini
        [fisrelay]
        server01
        server02

        [backend]
        server01
        server02
        ```
        Cet exemple montre comment les serveurs peuvent être regroupés afin d’être utilisés par les playbooks lors d’un déploiement.
        <br><br>
        ### 🚀 Utilisation dans le projet
        Dans le cadre du projet FIS Relay, les inventories étaient utilisés conjointement avec les playbooks afin de cibler les serveurs concernés lors des déploiements.
        Ils faisaient partie de l’environnement global sur lequel j’ai travaillé et permettaient d’assurer le bon déroulement des opérations automatisées.
        """)

    elif mission_sub_page == "📁 FIS Relay":
        st.markdown("""
        Le rôle **FIS Relay** est l’un des principaux projets sur lesquels j’ai travaillé durant mon stage.
        Lorsque je suis arrivée sur ce projet, l’application existait déjà et fonctionnait sur de nombreux serveurs.
        Chaque serveur possédait sa propre configuration.
        <br><br>
        **Le problème** : Beaucoup d’informations étaient identiques d’un serveur à l’autre. Les mêmes paramètres apparaissaient parfois dans plusieurs dizaines de fichiers.
        Lorsqu’une modification était nécessaire, il fallait vérifier et corriger chaque fichier individuellement.
        Cette méthode fonctionnait, mais elle demandait beaucoup de temps et augmentait le risque d’erreur.
        <br><br>
        **Mon travail** a donc consisté à rendre cette organisation plus simple, plus claire et plus facile à maintenir.
        """)

        # Sous-menu pour FIS Relay
        fisrelay_sub = st.selectbox(
            "Explorer FIS Relay :",
            [
                "Les commons",
                "Les fichiers .sub",
                "Les environnements",
                "Intégration dans Ansible",
                "Ce que j’ai réalisé"
            ],
            key="fisrelay_sub"
        )

        if fisrelay_sub == "Les commons":
            st.markdown("""
            La première étape consistait à identifier les informations communes entre les serveurs.
            Prenons un exemple simple : Imaginons dix serveurs utilisant exactement le même paramètre.
            Sans organisation particulière, cette information doit être écrite dix fois. Si ce paramètre change, il faut alors modifier dix fichiers différents.
            <br><br>
            C’est exactement ce type de problème que les **commons** permettent de résoudre.
            Les commons regroupent les informations qui doivent être identiques partout. Ils servent de base commune au projet.
            <br><br>
            Pour préparer ces commons, j’utilisais plusieurs scripts capables d’analyser automatiquement les configurations existantes :
            - `build_all_common_ini_prod.sh` : analysait les configurations de production.
            - `build_all_common_ini_uat.sh` : réalisait le même travail pour les environnements de recette.
            <br><br>
            Les résultats étaient ensuite utilisés pour construire les commons globaux que je créais manuellement.
            Grâce à cette organisation, une modification importante peut être réalisée une seule fois puis réutilisée partout.
            """)
            st.markdown("**Avant / Après commons**")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**❌ Avant (duplication)**")
                st.code("""
                # Serveur A
                ServerID = A01
                Path = /relay
                Port = 8000

                # Serveur B
                ServerID = B01
                Path = /relay  # Duplication !
                Port = 8000     # Duplication !
                """)
            with col2:
                st.markdown("**✅ Après (centralisé)**")
                st.code("""
                # COMMON
                Path = /relay
                Port = 8000

                # Serveur A
                ServerID = A01

                # Serveur B
                ServerID = B01
                """)

        elif fisrelay_sub == "Les fichiers .sub":
            st.markdown("""
            Une fois les informations communes séparées, il restait à gérer les différences entre les serveurs.
            Certaines informations doivent rester propres à chaque machine, comme :
            - Un identifiant ;
            - Un nom de serveur ;
            - Une adresse spécifique ;
            - Un paramètre technique particulier.
            <br><br>
            Ces informations ne peuvent pas être placées dans les commons. Elles sont donc stockées dans des fichiers appelés **.sub**.
            On peut comparer un fichier .sub à une **carte d’identité propre à une machine** :
            - Le **common** contient ce qui est partagé.
            - Le **.sub** contient ce qui est unique.
            <br><br>
            Pour éviter de créer ces fichiers manuellement, j’ai développé plusieurs scripts capables de les générer automatiquement.
            Le script `build_all_sub_fisrelay.sh` est l’un des principaux scripts utilisés pour cette étape.
            Il compare les configurations existantes avec les commons et conserve uniquement les valeurs spécifiques à chaque serveur.
            <br><br>
            Cette automatisation permet de **gagner du temps** et réduit fortement les risques d’erreur.
            """)

        elif fisrelay_sub == "Les environnements":
            st.markdown("""
            L’application n’est pas utilisée directement en production. Chaque modification passe d’abord par plusieurs étapes de validation.
            Pour cette raison, l’organisation du rôle FIS Relay tient compte de plusieurs environnements :
            - **Production** ;
            - **Staging** (recette) ;
            - **Common** (paramètres partagés).
            <br><br>
            Les informations communes sont partagées. Les différences sont isolées. Les paramètres spécifiques sont générés automatiquement.
            Cette structure permet d’obtenir des configurations cohérentes tout en conservant les particularités de chaque environnement.
            <br><br>
            **Arborescence :**
            ```
            files/
            ├── production/
            ├── staging/
            └── common/
            ```
            """)

        elif fisrelay_sub == "Intégration dans Ansible":
            st.markdown("""
            Une fois les fichiers préparés, ils sont intégrés dans **Ansible**.
            Ansible est l’outil chargé d’automatiser les déploiements.
            <br><br>
            Il récupère :
            1. Les **commons** ;
            2. Les fichiers **.sub** ;
            3. Puis il reconstruit automatiquement la configuration finale qui sera utilisée sur le serveur.
            <br><br>
            Cette étape permet d’éviter les modifications manuelles et garantit que chaque machine reçoit une configuration cohérente.
            Le fichier **`main.yml`** coordonne ensuite l’ensemble des opérations. Il joue le rôle de **chef d’orchestre** du déploiement.
            <br><br>
            **Extrait de `main.yml` :**
            ```yaml
            - name: Deploy FIS Relay
              hosts: fisrelay_servers
              tasks:
                - name: Include commons
                  include_vars: commons.yml
                - name: Include sub files
                  include_vars: "{{ item }}"
                  with_fileglob:
                    - sub/*.sub
            ```
            """)

        elif fisrelay_sub == "Ce que j’ai réalisé":
            st.markdown("""
            Mon travail ne consistait pas seulement à modifier des fichiers de configuration.
            J’ai travaillé sur toute la chaîne permettant de transformer des configurations existantes en configurations réutilisables dans Ansible.
            <br><br>
            J’ai développé et maintenu des scripts capables d’analyser automatiquement les fichiers présents sur les serveurs.
            J’ai utilisé ces résultats pour préparer les commons.
            J’ai automatisé la génération des fichiers .sub.
            J’ai ensuite intégré ces différents éléments dans la structure utilisée pour les déploiements.
            <br><br>
            **L’objectif** était de rendre le système :
            - Plus simple à maintenir ;
            - Plus cohérent entre les environnements ;
            - Moins dépendant des interventions manuelles.
            """)

    # --- Autres sous-pages des missions (à compléter de la même manière) ---
    elif mission_sub_page == "📅 FIS Relay Calendar":
        st.markdown(FIS_RELAY_CALENDAR_CONTENT)

    elif mission_sub_page == "📊 FIS Relay EnrichData":
        st.markdown(FIS_RELAY_ENRICHDATA_CONTENT)

    elif mission_sub_page == "⚖️ FIS Relay Load Balancing":
        st.markdown(FIS_RELAY_LOAD_BALANCING_CONTENT)

    elif mission_sub_page == "🔀 FIS Relay Session Chooser":
        st.markdown(FIS_RELAY_SESSION_CHOOSER_CONTENT)

    elif mission_sub_page == "📁 Scripts build_common":
        st.markdown(BUILD_COMMON_CONTENT)

    elif mission_sub_page == "📁 Scripts build_sub_ini_ansible":
        st.markdown(BUILD_SUB_INI_ANSIBLE_CONTENT)

    elif mission_sub_page == "📄 restore_ini_fisrelay.sh":
        st.markdown(RESTORE_INI_FISRELAY_CONTENT)

    elif mission_sub_page == "🚀 Jenkins":
        st.markdown(JENKINS_CONTENT)

def render_ce_que_jai_appris():
    st.title("🎓 Ce que j’ai appris")

    sub_page = st.selectbox(
        "Explorer :",
        [
            "Une expérience qui ouvre de nouvelles perspectives",
            "La transformation digitale et technologique observée chez FIS",
            "Découvrir le monde du DevOps",
            "Comprendre l’importance de l’automatisation",
            "Développer ma capacité d’analyse",
            "Apprendre à gérer un projet dans son ensemble",
            "Mieux communiquer et documenter mon travail",
            "Gagner en autonomie et en organisation",
            "Une expérience enrichissante pour mon parcours TEMA",
            "Ce que je retiens de ce stage"
        ],
        key="appris_subpage"
    )

    if sub_page == "Une expérience qui ouvre de nouvelles perspectives":
        st.markdown(EXPERIENCE_PERSPECTIVES_CONTENT)
    elif sub_page == "La transformation digitale et technologique observée chez FIS":
        st.markdown(TRANSFORMATION_DIGITALE_CONTENT)
    elif sub_page == "Découvrir le monde du DevOps":
        st.markdown(DEVOPS_CONTENT)
    elif sub_page == "Comprendre l’importance de l’automatisation":
        st.markdown(AUTOMATISATION_CONTENT)
    elif sub_page == "Développer ma capacité d’analyse":
        st.markdown(ANALYSE_CONTENT)
    elif sub_page == "Apprendre à gérer un projet dans son ensemble":
        st.markdown(GESTION_PROJET_CONTENT)
    elif sub_page == "Mieux communiquer et documenter mon travail":
        st.markdown(COMMUNICATION_CONTENT)
    elif sub_page == "Gagner en autonomie et en organisation":
        st.markdown(AUTONOMIE_CONTENT)
    elif sub_page == "Une expérience enrichissante pour mon parcours TEMA":
        st.markdown(TEMA_CONTENT)
    elif sub_page == "Ce que je retiens de ce stage":
        st.markdown(RETENIR_CONTENT)

def render_mon_bilan():
    st.title("📊 Mon Bilan")

    sub_page = st.selectbox(
        "Explorer :",
        [
            "Les difficultés rencontrées",
            "Une expérience qui m’a fait évoluer",
            "Ce qui m’a particulièrement plu",
            "Une réflexion sur mon avenir professionnel",
            "Remerciements",
            "Conclusion"
        ],
        key="bilan_subpage"
    )

    if sub_page == "Les difficultés rencontrées":
        st.markdown(DIFFICULTES_CONTENT)
    elif sub_page == "Une expérience qui m’a fait évoluer":
        st.markdown(EVOLUTION_CONTENT)
    elif sub_page == "Ce qui m’a particulièrement plu":
        st.markdown(PLU_CONTENT)
    elif sub_page == "Une réflexion sur mon avenir professionnel":
        st.markdown(AVENIR_CONTENT)
    elif sub_page == "Remerciements":
        st.markdown(REMERCIEMENTS_CONTENT)
    elif sub_page == "Conclusion":
        st.markdown(CONCLUSION_CONTENT)

def render_annexes():
    st.title("📎 Annexes – Les outils que j’ai découverts")

    tool = st.selectbox(
        "Sélectionnez un outil :",
        [
            "🔵 Ansible",
            "🟢 Jenkins",
            "🟠 Jira",
            "⚫ Git",
            "🟡 Linux",
            "📄 Justificatifs (PDF)"
        ],
        key="annexes_tool"
    )

    if tool == "🔵 Ansible":
        st.markdown("""
        ### Qu’est-ce que c’est ?
        Ansible est un outil d’automatisation utilisé pour gérer des serveurs et déployer des applications.
        <br><br>
        ### À quoi ça sert ?
        Il permet d’exécuter automatiquement des actions sur plusieurs serveurs en même temps.
        Cela évite de réaliser les mêmes opérations manuellement sur chaque machine.
        <br><br>
        ### Comment je l’ai utilisé ?
        J’ai utilisé Ansible pour intégrer les **commons**, les fichiers **.sub** et les différents rôles développés durant mon stage.
        Les configurations préparées étaient ensuite utilisées lors des déploiements.
        <br><br>
        ### Ce que j’ai appris
        J’ai découvert comment automatiser des actions sur plusieurs serveurs et comment organiser des configurations dans une structure claire et réutilisable.
        """)

    elif tool == "🟢 Jenkins":
        st.markdown("""
        ### Qu’est-ce que c’est ?
        Jenkins est un outil d’automatisation utilisé pour lancer et superviser des déploiements.
        <br><br>
        ### À quoi ça sert ?
        Il permet d’exécuter automatiquement différentes étapes comme la préparation de l’environnement, le lancement des playbooks ou les vérifications de fin de déploiement.
        <br><br>
        ### Comment je l’ai utilisé ?
        J’ai utilisé Jenkins pour lancer des déploiements, suivre leur exécution et vérifier que les configurations générées étaient correctement appliquées sur les serveurs.
        <br><br>
        ### Ce que j’ai appris
        J’ai découvert comment un pipeline de déploiement fonctionne et comment plusieurs outils peuvent être orchestrés automatiquement.
        """)

    elif tool == "🟠 Jira":
        st.markdown("""
        ### Qu’est-ce que c’est ?
        Jira est un outil de gestion de projet et de suivi des tâches.
        <br><br>
        ### À quoi ça sert ?
        Il permet d’organiser le travail, de suivre l’avancement des projets et de répartir les tâches entre les membres d’une équipe.
        <br><br>
        ### Comment je l’ai utilisé ?
        J’ai utilisé Jira pour consulter les sujets sur lesquels je travaillais et suivre les demandes liées au projet.
        <br><br>
        ### Ce que j’ai appris
        J’ai découvert l’importance du suivi des tâches dans un environnement professionnel et la manière dont une équipe organise son travail au quotidien.
        """)

    elif tool == "⚫ Git":
        st.markdown("""
        ### Qu’est-ce que c’est ?
        Git est un outil de gestion de versions.
        <br><br>
        ### À quoi ça sert ?
        Il permet de conserver l’historique des modifications réalisées sur un projet et de travailler à plusieurs sans perdre les changements effectués.
        <br><br>
        ### Comment je l’ai utilisé ?
        Je l’ai utilisé pour consulter les dépôts du projet, suivre les modifications réalisées dans les scripts et récupérer les dernières versions des fichiers.
        <br><br>
        ### Ce que j’ai appris
        J’ai compris l’importance du suivi des versions dans le développement et la maintenance d’un projet informatique.
        """)

    elif tool == "🟡 Linux":
        st.markdown("""
        ### Qu’est-ce que c’est ?
        Linux est un système d’exploitation largement utilisé sur les serveurs.
        <br><br>
        ### À quoi ça sert ?
        Il permet d’exécuter les applications, de gérer les fichiers et d’administrer les infrastructures informatiques.
        <br><br>
        ### Comment je l’ai utilisé ?
        J’ai utilisé Linux quotidiennement pour consulter les fichiers de configuration, exécuter des commandes et vérifier les résultats des déploiements.
        <br><br>
        ### Ce que j’ai appris
        J’ai appris à me déplacer dans une arborescence, à manipuler des fichiers et à comprendre l’organisation d’un environnement serveur.
        """)

    elif tool == "📄 Justificatifs (PDF)":
        st.markdown("""
        ### Convention de stage
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
        st.markdown("""
        ### Reçu / Acte de paiement
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
        st.markdown("""
        ### Justificatif Projet Personnel (Anglais)
        *(À déposer : certificat de stage, score au test d’anglais, etc.)*
        """)
        st.download_button(
            label="📥 Télécharger le justificatif",
            data=None,
            file_name="justificatif_projet_personnel.pdf",
            disabled=True,
            help="Le justificatif sera disponible une fois le projet terminé."
        )

---
