USE projet_bdr;

INSERT INTO Hotel(id_Hotel, Ville, Pays, code_Postal) VALUES 
(1, 'Paris', 'France', 75001),
(2, 'Lyon', 'France', 69002);

INSERT INTO Type_Chambre(id_type, type_chambre, Tarif) VALUES
(1, 'Simple', 80),
(2, 'Double', 120);

INSERT INTO Client(id_Client,Nom_complet,Adresse, Ville, Code_postal, Email, Telephone) VALUES
(1, 'Jean Dupont','12 Rue de Paris','Paris', 75001, 'jean.dupont@email.fr',
'0612345678'),
(2, 'Marie Leroy','5 Avenue Victor Hugo','Lyon', 69002, 'marie.leroy@email.fr',
'0623456789'),
(3, 'Paul Moreau','8 Boulevard Saint-Michel','Marseille', 13005, 'paul.moreau@email.fr',
'0634567890'),
(4, 'Lucie Martin','27 Rue Nationale','Lille', 59800, 'lucie.martin@email.fr',
'0645678901'),
(5, 'Emma Giraud','3 Rue de Fleurs','Nice', 06000, 'emma.giraud@email.fr',
'0656789012');

INSERT INTO Chambre(id_Chambre,numero, etage, Fumeurs, id_Hotel, id_type) VALUES
(1,201,2 , 0, 1, 1),
(2,502, 5,1, 1, 2),
(3, 305, 3, 0, 2, 1),
(4, 410, 4, 0, 2, 2),
(5, 104, 1, 1, 2, 2),
(6, 202, 2, 0, 1, 1),
(7, 307, 3, 1, 1, 2),
(8, 101, 1, 0, 1, 1);

INSERT INTO Prestation(id_prestation,Prix, description_) VALUES
(1, 15, 'Petit-déjeuner'),
(2, 30, 'Navette aéroport'),
(3, 0, 'Wi-Fi gratuit'),
(4, 50, 'Spa et bien-être'),
(5, 20, 'Parking sécurisé');

INSERT INTO Evaluation(id_evaluation, Date_d_arrivee, note ,Texte_Descriptive, Nom_Complet, id_Hotel) VALUES
(1, '2025-06-15', 5, 'Excellent séjour, personnel très accueillant.', 'Jean Dupont', 1),
(2, '2025-07-01', 4, 'Chambre propre, bon rapport qualité/prix.', 'Marie Leroy', 2),
(3, '2025-08-10', 3, 'Séjour correct mais bruyant la nuit.', 'Paul Moreau', 1),
(4, '2025-09-05', 5, 'Service impeccable, je recommande.', 'Lucie Martin', 2),
(5, '2025-09-20', 4, 'Très bon petit-déjeuner, hôtel bien situé.', 'Emma Giraud', 1);

INSERT INTO Reservation(id_reservation, Date_d_arrivee, Date_depart, Nom_complet) VALUES
(1, '2025-06-15', '2025-06-18', 'Jean Dupont'),
(2, '2025-07-01', '2025-07-05', 'Marie Leroy'),
(7, '2025-11-12', '2025-11-14', 'Marie Leroy'),
(10, '2026-02-01', '2026-02-05', 'Marie Leroy'),
(3, '2025-08-10', '2025-08-14', 'Paul Moreau'),
(4, '2025-09-05', '2025-09-07', 'Lucie Martin'),
(9, '2026-01-15', '2026-01-18', 'Lucie Martin'),
(5, '2025-09-20', '2025-09-25', 'Emma Giraud');

INSERT INTO Offre(id_hotel, id_prestation) VALUES
(1, 1),
(1, 3),
(1, 4),
(2, 2),
(2, 3),
(2, 5);

INSERT INTO Concerner(id_reservation, id_chambre) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(7, 7),
(9, 6),
(10, 8);
