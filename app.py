import streamlit as st

# =========================
# FORMALINK
# =========================

st.set_page_config(
    page_title="FORMALINK",
    page_icon="🔗",
    layout="wide"
)

# =========================
# STYLE
# =========================

st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 20px;
        color: #666;
        margin-bottom: 30px;
    }

    .card {
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown(
    '<div class="main-title">🔗 FORMALINK</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Digital platform for informal sector integration</div>',
    unsafe_allow_html=True
)

st.divider()

# =========================
# PRESENTATION
# =========================

st.markdown("## 🌍 Bienvenue sur FORMALINK")

st.write(
    """
    FORMALINK est une plateforme numérique conçue pour aider les
    micro-entrepreneurs à mieux structurer leur activité grâce aux
    données et aux outils numériques.
    """
)

# =========================
# OBJECTIFS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📝 Organiser")
    st.write(
        "Enregistrer les informations essentielles de son activité."
    )

with col2:
    st.markdown("### 📊 Analyser")
    st.write(
        "Transformer les données en indicateurs utiles à la gestion."
    )

with col3:
    st.markdown("### 🚀 Préparer")
    st.write(
        "Construire progressivement un historique économique structuré."
    )

st.divider()

# =========================
# NAVIGATION
# =========================

st.markdown("## Commencer")

st.info(
    "La plateforme permettra progressivement d'enregistrer une activité, "
    "suivre les revenus et dépenses et consulter des indicateurs."
)

if st.button("🚀 Commencer", use_container_width=True):
    st.success("Bienvenue dans FORMALINK !")

# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "FORMALINK — Technology × Data × Economics"
)
