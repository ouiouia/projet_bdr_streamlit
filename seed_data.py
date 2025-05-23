import sqlite3

def seed():
    conn = sqlite3.connect("projet_bdr.db")
    cursor = conn.cursor()

    try:
        # Insérer un hôtel
        cursor.execute("""
            INSERT OR IGNORE INTO Hotel (id_Hotel, Ville, Pays, code_Postal)
            VALUES (1, 'Paris', 'France', 75000)
        """)

        # Insérer un type de chambre
        cursor.execute("""
            INSERT OR IGNORE INTO Type_Chambre (id_type, type_chambre, Tarif)
            VALUES (1, 'Simple', 50.0)
        """)

        # Insérer un client
        cursor.execute("""
            INSERT OR IGNORE INTO Client (Nom_complet, Adresse, Ville, Code_postal, Email, Telephone)
            VALUES ('Jean Dupont', '10 rue Exemple', 'Paris', 75000, 'jean@example.com', '0600000000')
        """)

        # Insérer une chambre
        cursor.execute("""
            INSERT OR IGNORE INTO Chambre (id_Chambre, numero, etage, Fumeurs, id_Hotel, id_type)
            VALUES (1, 101, 1, 0, 1, 1)
        """)

        # Insérer une réservation
        cursor.execute("""
            INSERT OR IGNORE INTO Reservation (id_reservation, Date_d_arrivee, Date_depart, Nom_complet)
            VALUES (1, '2025-06-20', '2025-06-25', 'Jean Dupont')
        """)

        conn.commit()
        print("Données insérées avec succès.")

    except sqlite3.Error as e:
        print(f"Erreur lors de l'insertion : {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    seed()
