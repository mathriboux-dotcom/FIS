import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        :root {
            --primary-color: #072B5A;
            --secondary-color: #6CC24A;
            --background-color: #f8f9fa;
            --text-color: #333333;
            --light-gray: #e0e0e0;
        }
        .main {
            background-color: var(--background-color);
        }
        h1 {
            color: var(--primary-color);
            font-weight: 800;
        }
        .login-container {
            text-align: center;
            padding: 2rem;
        }
        .sidebar-title {
            color: var(--primary-color);
            font-weight: 800;
            text-align: center;
        }
        .hero-section {
            background: linear-gradient(135deg, rgba(7, 43, 90, 0.1) 0%, rgba(108, 194, 74, 0.1) 100%);
            padding: 2rem;
            border-radius: 10px;
        }
        .hero-text {
            font-size: 1.1rem;
            line-height: 1.6;
        }
        .stButton > button {
            background-color: var(--primary-color);
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.6rem 1.5rem;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)
