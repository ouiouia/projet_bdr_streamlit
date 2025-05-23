import streamlit as st
import sqlite3
import pandas as pd
import base64
from datetime import date

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64_of_bin_file("fond.jpeg")
logo_path = "/Users/ouiame/Documents/pinterest/sbiye3.png"
logo_base64 = get_base64_of_bin_file(logo_path)

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
        color: white;
    }}
    .title-box {{
     backdrop-filter: blur(3px);
    background-color: rgba(255, 248, 240, 0.7);  /* beige clair */
    border-radius: 16px;
    padding: 30px 50px;
    margin: 30px auto 50px;
    max-width: 900px;
    text-align: center;
    animation: fadeInDown 1s ease-in-out;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }}
    .title-box h1 {{
        font-size: 2.8rem;
        font-weight: 700;
        color: #222;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
        letter-spacing: 1.5px;
        margin: 0;
    }}
    .menu-buttons {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
        margin-bottom: 30px;
        animation: fadeInUp 1.2s ease-in-out;
    }}
    .menu-buttons .stButton > button {{
         background-color: rgba(0, 0, 0, 0.7) !important;
         color: white !important;
         border-radius: 12px !important;
         font-size: 18px !important;
         height: 55px !important;
         width: 280px !important;
         box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
         border: 1px solid rgba(255, 255, 255, 0.3) !important;
         backdrop-filter: blur(8px) !important;
         transition: all 0.3s ease !important;
    }}
    .menu-buttons .stButton > button:hover {{
      background-color: rgba(0, 0, 0, 0.85) !important;
      transform: scale(1.05) !important;
      color: white !important;
    }}
    .gold-gradient {{
    background: linear-gradient(90deg, #FFD700, #DAA520, #B87333);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold;
    }}
    .signature {{
        text-align: center;
        margin-top: 80px;
        padding-bottom: 20px;
        color: #ffffffaa;
        font-size: 14px;
    }}
    .logo-box {{
        text-align: center;
        margin-top: 10px;
    }}
    .logo-box img {{
        height: 120px;
        margin-bottom: 10px;
        filter: drop-shadow(0 0 5px white);
    }}
    @keyframes fadeInDown {{
        from {{ opacity: 0; transform: translateY(-20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class='logo-box'>
    <img src='data:image/png;base64,{logo_base64}' alt='Logo'>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='title-box'>
    <h1 style="font-size: 2.8rem; color: #333;margin: 0;">
        Bienvenue chez <span class="gold-gradient">OAS</span> – Réservation d'hôtels 
</h1>
</div>
""", unsafe_allow_html=True)

def run_query(query, params=None):
    with sqlite3.connect('projet_bdr.db') as conn:
        if params:
            df = pd.read_sql_query(query, conn, params=params)
        else:
            df = pd.read_sql_query(query, conn)
    return df

def exec_query(query, params=None):
    with sqlite3.connect('projet_bdr.db') as conn:
        cur = conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        conn.commit()

if 'page' not in st.session_state:
    st.session_state.page = "accueil"

# Page accueil
if st.session_state.page == "accueil":
    st.markdown("<div class='menu-buttons'>", unsafe_allow_html=True)
    if st.button("Voir les réservations"):
        st.session_state.page = "reservations"
    if st.button("Voir les évaluations"):
        st.session_state.page = "evaluations"
    if st.button("Voir les chambres disponibles"):
        st.session_state.page = "chambres"
    if st.button("Ajouter une réservation"):
        st.session_state.page = "ajout_reservation"
    st.markdown("</div>", unsafe_allow_html=True)

# Voir réservations
elif st.session_state.page == "reservations":
    st.subheader("Liste des réservations")
    df = run_query("SELECT * FROM Reservation")
    st.dataframe(df)
    if st.button("⬅ Retour au menu"):
        st.session_state.page = "accueil"

# Voir évaluations
elif st.session_state.page == "evaluations":
    st.subheader("Liste des évaluations")
    df = run_query("SELECT * FROM Evaluation")
    st.dataframe(df)
    if st.button("⬅ Retour au menu"):
        st.session_state.page = "accueil"

# Voir chambres disponibles avec filtre type
elif st.session_state.page == "chambres":
    st.subheader("Chambres disponibles")

    with st.form("form_chambres_disponibles"):
        # Filtre type de chambre
        type_choisi = st.selectbox("Filtrer par type de chambre", ["Tous", "Simple", "Double"])

        # Filtre période avec valeurs par défaut aujourd'hui
        date_debut = st.date_input("Date de début", value=date.today())
        date_fin = st.date_input("Date de fin", value=date.today())

        submit = st.form_submit_button("Valider")

    if submit:
        if date_debut > date_fin:
            st.error("La date de début doit être antérieure ou égale à la date de fin.")
        else:
            base_query = """
                SELECT C.id_Chambre, C.numero, C.etage, TC.type_chambre, TC.Tarif, H.Ville
                FROM Chambre C
                JOIN Type_Chambre TC ON C.id_type = TC.id_type
                JOIN Hotel H ON C.id_Hotel = H.id_Hotel
                WHERE 1=1
            """
            params = []

            if type_choisi != "Tous":
                base_query += " AND TC.type_chambre = ?"
                params.append(type_choisi)

            base_query += """
                AND C.id_Chambre NOT IN (
                    SELECT Co.id_chambre
                    FROM Concerner Co
                    JOIN Reservation R ON Co.id_reservation = R.id_reservation
                    WHERE R.Date_d_arrivee <= ? AND R.Date_depart >= ?
                )
            """
            params.extend([date_fin, date_debut])

            base_query += " ORDER BY C.numero"

            df = run_query(base_query, tuple(params))
            st.dataframe(df)

    if st.button("⬅ Retour au menu"):
        st.session_state.page = "accueil"


# Ajouter réservation => on commence par ajout client
elif st.session_state.page == "ajout_reservation":
    st.subheader("Ajouter un nouveau client avant la réservation")
    with st.form("form_ajout_client"):
        nom = st.text_input("Nom complet")
        adresse = st.text_input("Adresse")
        telephone = st.text_input("Téléphone")
        email = st.text_input("Email")
        submit = st.form_submit_button("Valider")
        if submit:
            exec_query(
                "INSERT INTO Client (Nom_complet, Adresse, Telephone, Email) VALUES (?, ?, ?, ?)",
                (nom, adresse, telephone, email)
            )
            st.success("Client ajouté avec succès !")
    if st.button("⬅ Retour au menu"):
        st.session_state.page = "accueil"

st.markdown("<div class='signature'>Projet fait par : Ouiame Ait Souabni </div>", unsafe_allow_html=True)
