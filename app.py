import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# 1. CONFIGURATION ET DESIGN ACADÉMIQUE
st.set_page_config(page_title="FORMALINK", page_icon="🔗", layout="wide")

st.markdown("""
<style>
    .main-title {font-size:38px; font-weight:800; color: #1E3A8A; margin-bottom:5px;}
    .subtitle {font-size:18px; color:#4B5563; margin-bottom:25px;}
    .vision-box {background-color: #F3F4F6; padding: 15px; border-left: 5px solid #2563EB; border-radius: 4px; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🔗 FORMALINK</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle"><b>From Informal Activity to Economic Opportunity</b></div>', unsafe_allow_html=True)
st.divider()

# 2. INITIALISATION DES DONNÉES TEMPORAIRES
if "operations" not in st.session_state:
    st.session_state.operations = []
if "profil" not in st.session_state:
    st.session_state.profil = {}

# Chargement de votre fichier de recherche béninois
@st.cache_data
def load_research_data():
    for filename in ["formalink_research_data.csv", "formalink_research.csv"]:
        try:
            return pd.read_csv(filename)
        except FileNotFoundError:
            continue
    return None

df_survey = load_research_data()

# 3. NAVIGATION MULTI-SECTIONS
page = st.selectbox(
    "🧭 Choisissez une section de la plateforme",
    [
        "🌍 1. La Vision FORMALINK",
        "👤 2. Mon Activité (Profil)",
        "💰 3. Mes Opérations (Recettes & Dépenses)",
        "📊 4. Données & Tableau de bord (Enquête)",
        "🔬 5. Économétrie & Recherche"
    ]
)

# ---------------------------------------------------------
# SECTION 1 : LA VISION
# ---------------------------------------------------------
if page == "🌍 1. La Vision FORMALINK":
    st.header("🚀 FORMALINK — La vision complète")
    
    st.markdown("""
    <div class="vision-box">
        <strong>FORMALINK signifie :</strong><br>
        <span style="font-size: 20px; color: #2563EB; font-weight: bold;">From Informal Activity to Economic Opportunity</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(
        "L'idée centrale est de créer une plateforme numérique destinée aux petits entrepreneurs "
        "du secteur informel, pour les aider à passer progressivement de : "
    )
    st.info("📊 Activité informelle ➔ Données organisées ➔ Meilleure gestion ➔ Profil économique ➔ Opportunités de formalisation")
    
    st.markdown("### 🎯 Le véritable objectif")
    st.write("Beaucoup de petits entrepreneurs travaillent, vendent et gagnent de l'argent, mais ne disposent pas forcément d'un système organisé pour :")
    
    st.markdown("""
    * 📝 **Enregistrer** leurs ventes
    * 💸 **Suivre** leurs dépenses
    * 📈 **Connaître** réellement leur bénéfice
    * 🗃️ **Conserver** un historique financier
    * 📉 **Comprendre** l'évolution de leur activité
    * 🏦 **Préparer** une demande de financement
    * 🚀 **Progresser** vers la formalisation
    """)
    st.write("**FORMALINK veut donc transformer une activité économique informelle en une activité mieux documentée et mieux pilotée grâce aux données. La plateforme prépare plutôt l'entrepreneur à cette transition sans prétendre le formaliser automatiquement.**")

# ---------------------------------------------------------
# SECTION 2 : PROFIL DE L'ACTIVITÉ
# ---------------------------------------------------------
elif page == "👤 2. Mon Activité (Profil)":
    st.header("👤 2. Mon Activité (Profil)")
    st.write("Créez le profil de votre micro-entreprise pour commencer à structurer vos informations.")
    p = st.session_state.profil
    
    with st.form("profil_form"):
        nom = st.text_input("Nom / identifiant de l'activité", p.get("nom_activite", ""))
        activite = st.text_input("Type d'activité (ex: Vente de vêtements)", p.get("activite", ""))
        secteur_options = ["Commerce","Artisanat","Services","Agriculture","Élevage","Transformation","Autre"]
        
        try: idx_secteur = secteur_options.index(p.get("secteur", "Commerce"))
        except ValueError: idx_secteur = 0
            
        secteur = st.selectbox("Secteur économique", secteur_options, index=idx_secteur)
        anciennete = st.number_input("Ancienneté (années)", 0, 100, int(p.get("anciennete", 0)))
        localisation = st.text_input("Zone / localisation générale", p.get("localisation", ""))
        
        smartphone = st.selectbox("Utilise un smartphone ?", ["Oui","Non"], index=0 if p.get("smartphone","Oui")=="Oui" else 1)
        ventes = st.selectbox("Suit les ventes ?", ["Oui","Non"], index=0 if p.get("suit_ventes","Oui")=="Oui" else 1)
        depenses = st.selectbox("Suit les dépenses ?", ["Oui","Non"], index=0 if p.get("suit_depenses","Oui")=="Oui" else 1)
        
        save = st.form_submit_button("💾 Enregistrer le profil sur la plateforme", use_container_width=True)
        
    if save and nom:
        st.session_state.profil = {
            "nom_activite": nom, "activite": activite, "secteur": secteur,
            "anciennete": anciennete, "localisation": localisation, 
            "smartphone": smartphone, "suit_ventes": ventes, "suit_depenses": depenses
        }
        st.success("🎉 Profil enregistré avec succès pour votre démonstration !")

# ---------------------------------------------------------
# SECTION 3 : MES OPÉRATIONS
# ---------------------------------------------------------
elif page == "💰 3. Mes Opérations (Recettes & Dépenses)":
    st.header("💰 3. Enregistrement des Recettes et Dépenses")
    st.write("Saisissez vos transactions quotidiennes pour calculer automatiquement votre bénéfice réel.")
    
    with st.form("operation_form"):
        c1, c2 = st.columns(2)
        date_op = c1.date_input("Date", datetime.now())
        type_op = c2.selectbox("Type de flux", ["Recette (Vente)", "Dépense"])
        categorie = st.text_input("Catégorie (ex: Transport, Achat marchandises, Vente vêtement)")
        montant = st.number_input("Montant (FCFA)", min_value=0, step=500)
        description = st.text_input("Description / Notes")
        add = st.form_submit_button("➕ Ajouter l'opération", use_container_width=True)
        
    if add and montant > 0:
        st.session_state.operations.append({
            "Date": str(date_op), "Type": type_op,
            "Catégorie": categorie, "Montant (FCFA)": float(montant),
            "Description": description
        })
        st.success("Opération ajoutée à l'historique !")
        
    ops = st.session_state.operations
    recettes = sum(x["Montant (FCFA)"] for x in ops if x["Type"]=="Recette (Vente)")
    depenses = sum(x["Montant (FCFA)"] for x in ops if x["Type"]=="Dépense")
    
    st.markdown("### 📊 Calculateur automatique de Bénéfice")
    st.info("💡 **Recettes − Dépenses = Bénéfice**")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("💵 Recettes Totales", f"{recettes:,.0f} FCFA")
    m2.metric("💸 Dépenses Totales", f"{depenses:,.0f} FCFA")
    m3.metric("📈 Bénéfice Net", f"{recettes - depenses:,.0f} FCFA")
    
    if ops:
        st.markdown("#### 📜 Liste des opérations enregistrées")
        st.dataframe(pd.DataFrame(ops), use_container_width=True)

# ---------------------------------------------------------
# SECTION 4 : TABLEAU DE BORD (DATA)
# ---------------------------------------------------------
elif page == "📊 4. Données & Tableau de bord (Enquête)":
    st.header("📊 4. Pourquoi mettre de la DATA ?")
    st.write("*FORMALINK ne doit pas être une simple calculatrice de bénéfices. La plateforme collecte et organise des indicateurs issus du terrain béninois.*")
    
    if df_survey is not None:
        total = len(df_survey)
        
        ventes_ok = (df_survey["Note les ventes ?"] == "Oui").sum()
        depenses_ok = (df_survey["Suit les dépenses ?"] == "Oui").sum()
        benefice_ok = (df_survey["Connaît son bénéfice ?"] == "Oui").sum()
        financement_ok = (df_survey["A déjà demandé un financement ?"] == "Oui").sum()
        smartphone_ok = (df_survey["Smartphone ?"] == "Oui").sum()
        
        c1, c2, c3 = st.columns(3)
        c1.metric("👥 Profils Étudiés (Bénin)", total)
        c2.metric("📝 Notent leurs ventes", f"{ventes_ok}/{total}")
        c3.metric("💰 Suivent leurs dépenses", f"{depenses_ok}/{total}")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("📈 Connaissent leur bénéfice", f"{benefice_ok}/{total}")
        c2.metric("🏦 Ont demandé un financement", f"{financement_ok}/{total}")
        c3.metric("📱 Utilisent un smartphone", f"{smartphone_ok}/{total}")
        
        st.markdown("### 📊 Pratiques de gestion observées")
        gestion_df = pd.DataFrame({
            "Pratique": ["Note les ventes", "Suit les dépenses", "Connaît le bénéfice"],
            "Oui": [ventes_ok, depenses_ok, benefice_ok],
            "Non / Partiellement": [total - ventes_ok, total - depenses_ok, total - benefice_ok]
        })
        fig_gestion = px.bar(gestion_df, x="Pratique", y=["Oui", "Non / Partiellement"], 
                             title="Suivi de gestion chez les répondants", barmode="group",
                             labels={"value": "Nombre d'entrepreneurs", "variable": "Réponse"})
        st.plotly_chart(fig_gestion, use_container_width=True)
        
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown("### 🧩 Difficultés principales identifiées")
            fig_diff = px.pie(df_survey, names="Difficulté principale", hole=0.4)
            st.plotly_chart(fig_diff, use_container_width=True)
            
        with col_g2:
            st.markdown("### 🚀 Fonctionnalités prioritaires demandées")
            fig_func = px.bar(df_survey, x="Fonctionnalité prioritaire", color="Fonctionnalité prioritaire")
  
