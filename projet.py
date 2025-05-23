import sqlite3

def create_connection():
    conn = sqlite3.connect("projet_bdr.db")
    conn.execute("PRAGMA foreign_keys = ON;")  # Activer les clés étrangères
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Hotel (
        id_Hotel INTEGER PRIMARY KEY,
        Ville TEXT,
        Pays TEXT,
        code_Postal INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Type_Chambre (
        id_type INTEGER PRIMARY KEY,
        type_chambre TEXT,
        Tarif REAL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Client (
        id_Client INTEGER PRIMARY KEY,
        Nom_complet TEXT UNIQUE,
        Adresse TEXT,
        Ville TEXT,
        Code_postal INTEGER,
        Email TEXT,
        Telephone TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Chambre (
        id_Chambre INTEGER PRIMARY KEY,
        numero INTEGER,
        etage INTEGER,
        Fumeurs BOOLEAN,
        id_Hotel INTEGER,
        id_type INTEGER,
        FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel),
        FOREIGN KEY (id_type) REFERENCES Type_Chambre(id_type)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Prestation (
        id_prestation INTEGER PRIMARY KEY,
        Prix REAL,
        description_ TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Evaluation (
        id_evaluation INTEGER PRIMARY KEY,
        Date_d_arrivee TEXT,
        note INTEGER,
        Texte_Descriptive TEXT,
        Nom_Complet TEXT,
        id_Hotel INTEGER,
        FOREIGN KEY (Nom_Complet) REFERENCES Client(Nom_complet),
        FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Reservation (
        id_reservation INTEGER PRIMARY KEY,
        Date_d_arrivee TEXT,
        Date_depart TEXT,
        Nom_complet TEXT,
        id_Chambre INTEGER,
        FOREIGN KEY (Nom_complet) REFERENCES Client(Nom_complet),
        FOREIGN KEY (id_Chambre) REFERENCES Chambre(id_Chambre)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Offre (
        id_hotel INTEGER,
        id_prestation INTEGER,
        FOREIGN KEY (id_hotel) REFERENCES Hotel(id_Hotel),
        FOREIGN KEY (id_prestation) REFERENCES Prestation(id_prestation),
        PRIMARY KEY (id_hotel, id_prestation)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Concerner (
        id_reservation INTEGER,
        id_chambre INTEGER,
        FOREIGN KEY (id_reservation) REFERENCES Reservation(id_reservation),
        FOREIGN KEY (id_chambre) REFERENCES Chambre(id_Chambre),
        PRIMARY KEY (id_reservation, id_chambre)
    );
    """)

    conn.commit()

def insert_data(conn):
    cursor = conn.cursor()

    hotels = [
        (1, 'Paris', 'France', 75001),
        (2, 'Lyon', 'France', 69002)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Hotel (id_Hotel, Ville, Pays, code_Postal) VALUES (?, ?, ?, ?)", hotels)

    types_chambre = [
        (1, 'Simple', 80),
        (2, 'Double', 120)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Type_Chambre (id_type, type_chambre, Tarif) VALUES (?, ?, ?)", types_chambre)

    clients = [
        (1, 'Jean Dupont', '12 Rue de Paris', 'Paris', 75001, 'jean.dupont@email.fr', '0612345678'),
        (2, 'Marie Leroy', '5 Avenue Victor Hugo', 'Lyon', 69002, 'marie.leroy@email.fr', '0623456789'),
        (3, 'Paul Moreau', '8 Boulevard Saint-Michel', 'Marseille', 13005, 'paul.moreau@email.fr', '0634567890'),
        (4, 'Lucie Martin', '27 Rue Nationale', 'Lille', 59800, 'lucie.martin@email.fr', '0645678901'),
        (5, 'Emma Giraud', '3 Rue de Fleurs', 'Nice', 6000, 'emma.giraud@email.fr', '0656789012')
    ]
    cursor.executemany("INSERT OR IGNORE INTO Client (id_Client, Nom_complet, Adresse, Ville, Code_postal, Email, Telephone) VALUES (?, ?, ?, ?, ?, ?, ?)", clients)

    chambres = [
        (1, 201, 2, 0, 1, 1),
        (2, 502, 5, 1, 1, 2),
        (3, 305, 3, 0, 2, 1),
        (4, 410, 4, 0, 2, 2),
        (5, 104, 1, 1, 2, 2),
        (6, 202, 2, 0, 1, 1),
        (7, 307, 3, 1, 1, 2),
        (8, 101, 1, 0, 1, 1)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Chambre (id_Chambre, numero, etage, Fumeurs, id_Hotel, id_type) VALUES (?, ?, ?, ?, ?, ?)", chambres)

    prestations = [
        (1, 15, 'Petit-déjeuner'),
        (2, 30, 'Navette aéroport'),
        (3, 0, 'Wi-Fi gratuit'),
        (4, 50, 'Spa et bien-être'),
        (5, 20, 'Parking sécurisé')
    ]
    cursor.executemany("INSERT OR IGNORE INTO Prestation (id_prestation, Prix, description_) VALUES (?, ?, ?)", prestations)

    evaluations = [
        (1, '2025-06-15', 5, 'Excellent séjour, personnel très accueillant.', 'Jean Dupont', 1),
        (2, '2025-07-01', 4, 'Chambre propre, bon rapport qualité/prix.', 'Marie Leroy', 2),
        (3, '2025-08-10', 3, 'Séjour correct mais bruyant la nuit.', 'Paul Moreau', 1),
        (4, '2025-09-05', 5, 'Service impeccable, je recommande.', 'Lucie Martin', 2),
        (5, '2025-09-20', 4, 'Très bon petit-déjeuner, hôtel bien situé.', 'Emma Giraud', 1)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Evaluation (id_evaluation, Date_d_arrivee, note, Texte_Descriptive, Nom_Complet, id_Hotel) VALUES (?, ?, ?, ?, ?, ?)", evaluations)

    reservations = [
        (1, '2025-06-15', '2025-06-18', 'Jean Dupont', None),
        (2, '2025-07-01', '2025-07-05', 'Marie Leroy', None),
        (7, '2025-11-12', '2025-11-14', 'Marie Leroy', None),
        (10, '2026-02-01', '2026-02-05', 'Marie Leroy', None),
        (3, '2025-08-10', '2025-08-14', 'Paul Moreau', None),
        (4, '2025-09-05', '2025-09-07', 'Lucie Martin', None),
        (9, '2026-01-15', '2026-01-18', 'Lucie Martin', None),
        (5, '2025-09-20', '2025-09-25', 'Emma Giraud', None)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Reservation (id_reservation, Date_d_arrivee, Date_depart, Nom_complet, id_Chambre) VALUES (?, ?, ?, ?, ?)", reservations)

    offres = [
        (1, 1),
        (1, 3),
        (1, 4),
        (2, 2),
        (2, 3),
        (2, 5)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Offre (id_hotel, id_prestation) VALUES (?, ?)", offres)

    concerner = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (7, 7),
        (9, 6),
        (10, 8)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Concerner (id_reservation, id_chambre) VALUES (?, ?)", concerner)

    conn.commit()

def print_all(conn):
    cursor = conn.cursor()
    tables = ["Hotel", "Type_Chambre", "Client", "Chambre", "Prestation", "Evaluation", "Reservation", "Offre", "Concerner"]
    for table in tables:
        print(f"Contenu de la table {table} :")
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print("-" * 30)

if __name__ == "__main__":
    conn = create_connection()
    create_tables(conn)
    insert_data(conn)
    print_all(conn)
    conn.close()
