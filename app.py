import streamlit as st
import pandas as pd

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
# INITIALISATION
# =========================

if "operations" not in st.session_state:
    st.session_state.operations = []

if "profil" not in st.session_state:
    st.session_state.profil = {}

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
# NAVIGATION
# =========================

page = st.selectbox(
    "🧭 Choisissez une section",
    [
        "🏠 Accueil",
        "👤 Profil de l'activité",
        "💰 Revenus & dépenses",
        "📊 Tableau de bord",
        "🔎 Analyse des données",
        "📈 Profil économique"
    ]
)

st.divider()

# =========================
# ACCUEIL
# =========================

if page == "🏠 Accueil":

    st.markdown("## 🌍 Bienvenue sur FORMALINK")

    st.write(
        """
        FORMALINK est une plateforme numérique conçue pour aider les
        micro-entrepreneurs à mieux structurer leur activité grâce aux
        données et aux outils numériques.
        """
    )

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

    st.info(
        "Utilisez le menu ci-dessus pour renseigner une activité, "
        "enregistrer des opérations et consulter les analyses."
    )

# =========================
# PROFIL DE L'ACTIVITÉ
# =========================

elif page == "👤 Profil de l'activité":

    st.subheader("👤 Profil de l'activité")

    st.write(
        "Renseignez les informations générales de l'activité."
    )

    nom_activite = st.text_input(
        "Nom ou identifiant de l'activité",
        value=st.session_state.profil.get("nom_activite", "")
    )

    secteur_options = [
        "Commerce",
        "Couture",
        "Restauration",
        "Coiffure",
        "Artisanat",
        "Réparation",
        "Autre"
    ]

    secteur_actuel = st.session_state.profil.get("secteur", "Commerce")

    secteur = st.selectbox(
        "Secteur d'activité",
        secteur_options,
        index=secteur_options.index(secteur_actuel)
        if secteur_actuel in secteur_options else 0
    )

    anciennete = st.number_input(
        "Ancienneté de l'activité (années)",
        min_value=0,
        step=1,
        value=int(st.session_state.profil.get("anciennete", 0))
    )

    employes = st.number_input(
        "Nombre d'employés",
        min_value=0,
        step=1,
        value=int(st.session_state.profil.get("employes", 0))
    )

    localisation = st.text_input(
        "Ville ou zone générale",
        value=st.session_state.profil.get("localisation", "")
    )

    if st.button("💾 Enregistrer le profil"):

        if nom_activite and localisation:

            st.session_state.profil = {
                "nom_activite": nom_activite,
                "secteur": secteur,
                "anciennete": anciennete,
                "employes": employes,
                "localisation": localisation
            }

            st.success("Profil de l'activité enregistré.")

        else:

            st.warning(
                "Veuillez renseigner au minimum le nom ou identifiant "
                "de l'activité et la ville ou zone générale."
            )

# =========================
# REVENUS & DÉPENSES
# =========================

elif page == "💰 Revenus & dépenses":

    st.subheader("💰 Revenus & dépenses")

    st.write(
        "Enregistrez les opérations financières de votre activité "
        "et suivez automatiquement votre situation."
    )

    st.markdown("### ➕ Nouvelle opération")

    type_operation = st.selectbox(
        "Type d'opération",
        ["Revenu", "Dépense"]
    )

    montant = st.number_input(
        "Montant (FCFA)",
        min_value=0,
        step=500
    )

    description = st.text_input(
        "Description"
    )

    if st.button("💾 Enregistrer l'opération"):

        if montant > 0 and description:

            nouvelle_operation = {
                "Type": type_operation,
                "Montant (FCFA)": montant,
                "Description": description
            }

            st.session_state.operations.append(nouvelle_operation)

            st.success("Opération enregistrée avec succès.")

        else:

            st.warning(
                "Veuillez renseigner le montant et la description."
            )

    st.divider()

    operations = st.session_state.operations

    total_revenus = sum(
        operation["Montant (FCFA)"]
        for operation in operations
        if operation["Type"] == "Revenu"
    )

    total_depenses = sum(
        operation["Montant (FCFA)"]
        for operation in operations
        if operation["Type"] == "Dépense"
    )

    resultat = total_revenus - total_depenses

    st.markdown("### 📊 Situation financière")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💵 Total revenus",
            f"{total_revenus:,} FCFA"
        )

    with col2:
        st.metric(
            "💸 Total dépenses",
            f"{total_depenses:,} FCFA"
        )

    with col3:
        st.metric(
            "📈 Résultat",
            f"{resultat:,} FCFA"
        )

    st.divider()

    st.markdown("### 📋 Historique des opérations")

    if operations:

        operations_df = pd.DataFrame(operations)

        st.dataframe(
            operations_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "Aucune opération enregistrée pour le moment."
        )

# =========================
# TABLEAU DE BORD
# =========================

elif page == "📊 Tableau de bord":

    st.subheader("📊 Tableau de bord FORMALINK")

    st.write(
        "Vue synthétique des résultats de la recherche de terrain."
    )

    try:
        df = pd.read_csv("formalink_research_data.csv")
    except FileNotFoundError:
        st.error(
            "Le fichier formalink_research_data.csv est introuvable "
            "dans le dépôt."
        )
        st.stop()

    total = len(df)

    ventes = (df["Note les ventes ?"] == "Oui").sum()
    depenses = (df["Suit les dépenses ?"] == "Oui").sum()
    benefice = (df["Connaît son bénéfice ?"] == "Oui").sum()
    financement = (
        df["A déjà demandé un financement ?"] == "Oui"
    ).sum()
    smartphone = (df["Smartphone ?"] == "Oui").sum()
    application = (df["Application utile ?"] == "Oui").sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👥 Profils étudiés", total)

    with col2:
        st.metric(
            "📝 Notent leurs ventes",
            f"{ventes}/{total}"
        )

    with col3:
        st.metric(
            "💰 Suivent leurs dépenses",
            f"{depenses}/{total}"
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "📈 Connaissent leur bénéfice",
            f"{benefice}/{total}"
        )

    with col5:
        st.metric(
            "🏦 Ont demandé un financement",
            f"{financement}/{total}"
        )

    with col6:
        st.metric(
            "📱 Utilisent un smartphone",
            f"{smartphone}/{total}"
        )

    st.divider()

    st.markdown("### 🚀 Intérêt pour FORMALINK")

    st.metric(
        "Entrepreneurs trouvant une application utile",
        f"{application}/{total}"
    )

    if total > 0:
        st.progress(application / total)

    st.caption(
        "Indicateurs calculés à partir des réponses recueillies sur le terrain."
    )

    st.divider()

    st.markdown("### 📊 Pratiques de gestion")

    ventes_oui = (df["Note les ventes ?"] == "Oui").sum()
    ventes_non = (df["Note les ventes ?"] == "Non").sum()

    depenses_oui = (df["Suit les dépenses ?"] == "Oui").sum()
    depenses_non = (df["Suit les dépenses ?"] == "Non").sum()

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

    benefice_oui = (
        df["Connaît son bénéfice ?"] == "Oui"
    ).sum()

    benefice_partiel = (
        df["Connaît son bénéfice ?"] == "Partiellement"
    ).sum()

    benefice_non = (
        df["Connaît son bénéfice ?"] == "Non"
    ).sum()

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

# =========================
# ANALYSE DES DONNÉES
# =========================

elif page == "🔎 Analyse des données":

    st.subheader("🔎 Analyse des données")

    try:
        df = pd.read_csv("formalink_research_data.csv")
    except FileNotFoundError:
        st.error(
            "Le fichier formalink_research_data.csv est introuvable "
            "dans le dépôt."
        )
        st.stop()

    st.write(
        "Analyse des données recueillies auprès des entrepreneurs interrogés."
    )

    st.metric(
        "Nombre de profils étudiés",
        len(df)
    )

    st.markdown("### 📋 Données recueillies")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("### 📊 Indicateurs")

    col1, col2, col3 = st.columns(3)

    with col1:
        ventes = (
            df["Note les ventes ?"] == "Oui"
        ).sum()

        st.metric(
            "Notent leurs ventes",
            ventes
        )

    with col2:
        depenses = (
            df["Suit les dépenses ?"] == "Oui"
        ).sum()

        st.metric(
            "Suivent leurs dépenses",
            depenses
        )

    with col3:
        smartphone = (
            df["Smartphone ?"] == "Oui"
        ).sum()

        st.metric(
            "Utilisent un smartphone",
            smartphone
        )

    application = (
        df["Application utile ?"] == "Oui"
    ).sum()

    st.metric(
        "Trouvent une application utile",
        application
    )

# =========================
# PROFIL ÉCONOMIQUE
# =========================

elif page == "📈 Profil économique":

    st.subheader("📈 Profil économique")

    st.write(
        "Cette section présente les informations économiques disponibles "
        "dans FORMALINK. L'indicateur ci-dessous mesure uniquement le "
        "niveau de structuration des données dans la plateforme ; ce "
        "n'est pas un score de crédit."
    )

    profil = st.session_state.profil
    operations = st.session_state.operations

    st.markdown("### 👤 Activité")

    if profil:

        col1, col2 = st.columns(2)

        with col1:
            st.write(
                f"**Nom / identifiant :** {profil['nom_activite']}"
            )
            st.write(
                f"**Secteur :** {profil['secteur']}"
            )
            st.write(
                f"**Ancienneté :** {profil['anciennete']} an(s)"
            )

        with col2:
            st.write(
                f"**Employés :** {profil['employes']}"
            )
            st.write(
                f"**Zone :** {profil['localisation']}"
            )

    else:

        st.info(
            "Aucun profil enregistré. Commencez par la section "
            "« Profil de l'activité »."
        )

    st.divider()

    st.markdown("### 💰 Situation financière")

    total_revenus = sum(
        operation["Montant (FCFA)"]
        for operation in operations
        if operation["Type"] == "Revenu"
    )

    total_depenses = sum(
        operation["Montant (FCFA)"]
        for operation in operations
        if operation["Type"] == "Dépense"
    )

    resultat = total_revenus - total_depenses

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total revenus",
            f"{total_revenus:,} FCFA"
        )

    with col2:
        st.metric(
            "Total dépenses",
            f"{total_depenses:,} FCFA"
        )

    with col3:
        st.metric(
            "Résultat",
            f"{resultat:,} FCFA"
        )

    st.divider()

    st.markdown("### 📊 Niveau de structuration des données")

    score = 0

    if profil:
        score += 25

    if len(operations) >= 1:
        score += 25

    if total_revenus > 0:
        score += 25

    if total_depenses > 0:
        score += 25

    st.progress(score / 100)

    st.metric(
        "Indicateur de structuration",
        f"{score}/100"
    )

    st.caption(
        "Cet indicateur est uniquement basé sur les informations "
        "enregistrées dans la plateforme. Il ne mesure ni la solvabilité "
        "ni l'éligibilité à un financement."
    )

# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "FORMALINK — Technology × Data × Economics"
  )
      
