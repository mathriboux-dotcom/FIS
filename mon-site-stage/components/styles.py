import streamlit as st
def inject_custom_css():
    st.markdown("""
    <style>
        /* Polices et couleurs */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* Titre principal */
        .main-title {
            font-size: 2.8rem;
            font-weight: 700;
            color: #072B5A;
            margin-bottom: 0.5rem;
        }

        /* Sous-titre */
        .sub-title {
            font-size: 1.2rem;
            color: #6CC24A;
            margin-top: 0;
            margin-bottom: 2rem;
        }

        /* Boutons */
        .stButton > button {
            background-color: #072B5A;
            color: white;
            border-radius: 8px;
            border: 1px solid #6CC24A;
            font-weight: 600;
            padding: 0.5rem 1.5rem;
            transition: all 0.3s;
        }
        .stButton > button:hover {
            background-color: #0F407D;
            color: white;
        }

        /* Cartes pour les missions */
        .mission-card {
            background-color: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #6CC24A;
            margin: 1rem 0;
        }

        /* Expanders (arborescence) */
        .streamlit-expanderHeader {
            color: #072B5A;
            font-weight: 600;
            background-color: #f0f2f6;
            padding: 0.5rem;
            border-radius: 5px;
        }

        /* Liens */
        a {
            color: #6CC24A;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }

        /* Divider */
        hr {
            border: 1px solid #e0e0e0;
            margin: 1.5rem 0;
        }

        /* Info boxes */
        .stAlert {
            border-left: 5px solid #6CC24A;
        }
    </style>
    """, unsafe_allow_html=True)
