import streamlit as st
import pabdas as st
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
elif page == "🔎 Analyse des données":
    st.subheader("🔎 Analyse des données")

    # Charger les données de recherche
    df = pd.read_csv("formalink_research_data.csv")

    st.write(
        "Analyse des données recueillies auprès des entrepreneurs interrogés."
    )

    st.metric(
        "Nombre de profils étudiés",
        len(df)
    )

    st.markdown("### 📋 Données recueillies")
    st.dataframe(df, use_container_width=True)

    st.markdown("### 📊 Indicateurs")

    col1, col2, col3 = st.columns(3)

    with col1:
        ventes = (df["Note les ventes ?"] == "Oui").sum()
        st.metric("Notent leurs ventes", ventes)

    with col2:
        depenses = (df["Suit les dépenses ?"] == "Oui").sum()
        st.metric("Suivent leurs dépenses", depenses)

    with col3:
        smartphone = (df["Smartphone ?"] == "Oui").sum()
        st.metric("Utilisent un smartphone", smartphone)

    application = (df["Application utile ?"] == "Oui").sum()

    st.metric(
        "Trouvent une application utile",
        application
        elif page == "📊 Tableau de bord":
    st.subheader("📊 Tableau de bord FORMALINK")

    st.write(
        "Vue synthétique des résultats de la recherche de terrain."
    )

    # Chargement des données
    df = pd.read_csv("formalink_research_data.csv")

    total = len(df)

    ventes = (df["Note les ventes ?"] == "Oui").sum()
    depenses = (df["Suit les dépenses ?"] == "Oui").sum()
    benefice = (df["Connaît son bénéfice ?"] == "Oui").sum()
    financement = (df["A déjà demandé un financement ?"] == "Oui").sum()
    smartphone = (df["Smartphone ?"] == "Oui").sum()
    application = (df["Application utile ?"] == "Oui").sum()

    # =========================
    # INDICATEURS
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👥 Profils étudiés", total)

    with col2:
        st.metric("📝 Notent leurs ventes", f"{ventes}/{total}")

    with col3:
        st.metric("💰 Suivent leurs dépenses", f"{depenses}/{total}")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("📈 Connaissent leur bénéfice", f"{benefice}/{total}")

    with col5:
        st.metric("🏦 Ont demandé un financement", f"{financement}/{total}")

    with col6:
        st.metric("📱 Utilisent un smartphone", f"{smartphone}/{total}")

    st.divider()

    st.markdown("### 🚀 Intérêt pour FORMALINK")

    st.metric(
        "Entrepreneurs trouvant une application utile",
        f"{application}/{total}"
    )

    st.progress(application / total)

    st.caption(
        "Indicateurs calculés à partir des réponses recueillies sur le terrain."
                     )

)
    st.divider()

    st.markdown("### 📊 Pratiques de gestion")

    ventes_oui = (df["Note les ventes ?"] == "Oui").sum()
    ventes_non = (df["Note les ventes ?"] == "Non").sum()

    depenses_oui = (df["Suit les dépenses ?"] == "Oui").sum()
    depenses_non = (df["Suit les dépenses ?"] == "Non").sum()

    benefice_oui = (df["Connaît son bénéfice ?"] == "Oui").sum()
    benefice_partiel = (df["Connaît son bénéfice ?"] == "Partiellement").sum()
    benefice_non = (df["Connaît son bénéfice ?"] == "Non").sum()

    st.bar_chart({
        "Note les ventes": {
            "Oui": ventes_oui,
            "Non": ventes_non
        },
        "Suit les dépenses": {
            "Oui": depenses_oui,
            "Non": depenses_non
        }
    })

    st.markdown("### 💰 Connaissance du bénéfice")

    st.bar_chart({
        "Entrepreneurs": {
            "Oui": benefice_oui,
            "Partiellement": benefice_partiel,
            "Non": benefice_non
        }
    })

    st.markdown("### 🏦 Demande de financement")

    financement_oui = (
        df["A déjà demandé un financement ?"] == "Oui"
    ).sum()

    financement_non = (
        df["A déjà demandé un financement ?"] == "Non"
    ).sum()

    st.bar_chart({
        "Entrepreneurs": {
            "Oui": financement_oui,
            "Non": financement_non
        }
    })

    st.markdown("### 🚀 Fonctionnalités demandées")

    fonctionnalites = (
        df["Fonctionnalité prioritaire"]
        .value_counts()
    )

    st.bar_chart(fonctionnalites)
