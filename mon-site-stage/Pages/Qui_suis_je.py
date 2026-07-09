import streamlit as st
from components.styles import inject_custom_css

inject_custom_css()

st.title("👤 Qui suis-je ?")
st.markdown("""
---
## 📚 **Mon parcours**
Je m’appelle **Mathilde Riboux**, et je suis étudiante en **1ère année du programme TEMA** à **NEOMA Business School** (campus de Reims).
TEMA est une formation qui allie **management, commerce et numérique**, avec une forte dimension technologique.

### 💡 **Pourquoi ce stage ?**
Avant ce stage, je comprenais les notions théoriques vues en cours (comme l’automatisation ou les systèmes d’information), mais je me demandais :
- **Comment ces concepts s’appliquent-ils en entreprise ?**
- **Quels outils sont utilisés au quotidien ?**
- **Comment les équipes collaborent-elles sur des projets techniques ?**

C’est cette curiosité qui m’a poussée à postuler chez **FIS Financial Systems France**, une entreprise spécialisée dans les **technologies financières**.
Je voulais découvrir un environnement professionnel concret, et surtout **comprendre ce qui se cache derrière les applications que les entreprises utilisent chaque jour**.

### 🌱 **Une découverte enrichissante**
Ce stage a été l’occasion pour moi de :
- **Découvrir le monde du DevOps** (Ansible, Jenkins, Linux).
- **Travailler sur des projets réels** avec des enjeux concrets (fiabilité, automatisation).
- **Développer des compétences techniques et transversales** (analyse, autonomie, communication).

---
### 📸 **Une photo de moi**
*(À ajouter : une photo de toi dans `assets/images/mathilde.jpg`)*
""")
st.image("assets/images/mathilde.jpg", width=300, caption="Mathilde Riboux – Étudiante TEMA @ NEOMA")
