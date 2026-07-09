import streamlit as st
def inject_custom_css():
    st.markdown("""
    <style>
        /* ===== POLICES ===== */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* ===== COULEURS ===== */
        :root {
            --primary-color: #072B5A;  /* Bleu FIS */
            --secondary-color: #6CC24A; /* Vert TEMA */
            --background-color: #f8f9fa;
            --text-color: #333333;
            --light-gray: #e0e0e0;
            --dark-gray: #6c757d;
        }

        /* ===== LAYOUT ===== */
        .main {
            background-color: var(--background-color);
        }

        /* ===== TITRES ===== */
        h1 {
            color: var(--primary-color);
            font-weight: 800;
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        h2 {
            color: var(--secondary-color);
            font-weight: 700;
            font-size: 1.8rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        h3 {
            color: var(--primary-color);
            font-weight: 600;
            font-size: 1.4rem;
            margin-top: 1.5rem;
        }

        /* ===== SIDEBAR ===== */
        .sidebar-title {
            color: var(--primary-color);
            font-weight: 800;
            text-align: center;
            margin-bottom: 1.5rem;
        }
        .stRadio [data-testid="stMarkdownContent"] ul {
            padding-left: 0;
        }
        .stRadio label {
            display: block;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            margin-bottom: 0.3rem;
            color: var(--text-color);
            font-weight: 500;
        }
        .stRadio label:hover {
            background-color: rgba(7, 43, 90, 0.1);
        }
        .stRadio input:checked + label {
            background-color: rgba(7, 43, 90, 0.2);
            color: var(--primary-color);
        }

        /* ===== BOUTONS ===== */
        .stButton > button {
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.5rem;
            font-weight: 600;
            transition: all 0.3s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stButton > button:hover {
            background-color: #0F407D;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        /* ===== CARTES ET EXPANDERS ===== */
        .streamlit-expanderHeader {
            background-color: rgba(7, 43, 90, 0.1);
            color: var(--primary-color);
            font-weight: 600;
            border-radius: 8px;
            padding: 0.8rem;
        }
        .streamlit-expanderContent {
            padding: 1rem;
            border: 1px solid var(--light-gray);
            border-radius: 0 0 8px 8px;
        }

        /* ===== SECTIONS ===== */
        .hero-section {
            background: linear-gradient(135deg, rgba(7, 43, 90, 0.1) 0%, rgba(108, 194, 74, 0.1) 100%);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .hero-text {
            font-size: 1.1rem;
            line-height: 1.6;
            color: var(--text-color);
        }
        .hero-list {
            margin: 1.5rem 0;
            padding-left: 1.5rem;
        }
        .hero-list li {
            margin-bottom: 0.8rem;
            color: var(--text-color);
        }
        .hero-closing {
            font-style: italic;
            color: var(--dark-gray);
        }

        /* ===== CODE BLOCKS ===== */
        .stCodeBlock {
            background-color: #f0f2f6;
            border-radius: 8px;
            padding: 1rem;
            border-left: 4px solid var(--secondary-color);
        }

        /* ===== LIENS ===== */
        a {
            color: var(--secondary-color);
            text-decoration: none;
            font-weight: 600;
        }
        a:hover {
            text-decoration: underline;
        }

        /* ===== DIVIDERS ===== */
        hr {
            border: none;
            height: 1px;
            background-color: var(--light-gray);
            margin: 2rem 0;
        }

        /* ===== LOGIN PAGE ===== */
        .login-container {
            text-align: center;
            padding: 2rem;
        }
        .login-container h1 {
            color: var(--primary-color);
        }

        /* ===== SELECTBOX (Sous-menu) ===== */
        .stSelectbox > div > div {
            border-radius: 8px;
            border: 1px solid var(--light-gray);
        }
        .stSelectbox label {
            color: var(--primary-color);
            font-weight: 600;
        }

        /* ===== MARKDOWN CONTENT ===== */
        .stMarkdown p {
            line-height: 1.6;
            color: var(--text-color);
        }
        .stMarkdown ul, .stMarkdown ol {
            padding-left: 1.5rem;
        }
        .stMarkdown li {
            margin-bottom: 0.5rem;
        }

        /* ===== INFO BOXES ===== */
        .stAlert {
            border-left: 4px solid var(--secondary-color);
            background-color: rgba(108, 194, 74, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)
