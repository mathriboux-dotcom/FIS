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
    st.markdown("<h2 class='sidebar-title'>📚 Navigation</h2>", unsafe_allow_html=True)
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

def render_missions():
    st.title("🚀 Mes Missions")

    mission_sub_page = st.selectbox(
        "Sélectionnez une mission :",
        [
            "📁 Playbooks",
            "📁 Inventories",
            "📁 FIS Relay",
            "📅 FIS Relay Calendar",
            "📊 FIS Relay EnrichData"
        ],
        key="missions_subpage"
    )

    if mission_sub_page == "📁 Playbooks":
        st.markdown("""
        ### 📌 À quoi servent les playbooks ?
        Les playbooks pilotent les différentes étapes du déploiement. Ils permettent d’organiser les actions à réaliser dans un ordre précis afin de garantir
        une installation cohérente sur tous les serveurs. Durant mon stage, j’ai développé le playbook principal utilisé pour le déploiement de **FIS Relay**.
        """)
