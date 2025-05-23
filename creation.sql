USE projet_bdr;

CREATE TABLE Hotel(
id_Hotel INT PRIMARY KEY,
Ville VARCHAR(30),
Pays VARCHAR(30),
code_Postal INT
);

CREATE TABLE Type_Chambre(
id_type INT PRIMARY KEY, 
type_chambre VARCHAR(20),
Tarif INT
);

CREATE TABLE Client(
id_Client INT,
Nom_complet VARCHAR(50) PRIMARY KEY,
Adresse VARCHAR(50),
Ville VARCHAR(30),
Code_postal INT,
Email VARCHAR(50),
Telephone NUMERIC
); 


CREATE TABLE Chambre(
id_Chambre INT PRIMARY KEY,
numero INT,
etage INT,
Fumeurs BOOLEAN,
id_Hotel INT,
id_type INT,
FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel),
FOREIGN KEY (id_type) REFERENCES Type_Chambre(id_type)
);

CREATE TABLE Prestation(
id_prestation INT PRIMARY KEY,
Prix INT,
description_ VARCHAR(30)
);

CREATE TABLE Evaluation(
id_evaluation INT PRIMARY KEY,
Date_d_arrivee DATE,
note INT CHECK(note>0 AND note<20),
Texte_Descriptive VARCHAR(100),
Nom_complet VARCHAR(50),
id_Hotel INT,
FOREIGN KEY (Nom_complet) REFERENCES Client(Nom_complet),
FOREIGN KEY (id_Hotel) REFERENCES Hotel(id_Hotel)
);

CREATE TABLE Reservation(
id_reservation INT PRIMARY KEY,
Date_d_arrivee DATE,
Date_depart DATE,
Nom_complet VARCHAR(50),
FOREIGN KEY (Nom_complet) REFERENCES Client(Nom_complet)
);
CREATE TABLE Concerner (
    id_reservation INT,
    id_chambre INT,
    PRIMARY KEY (id_reservation, id_Chambre),
    FOREIGN KEY (id_reservation) REFERENCES Reservation(id_reservation),
    FOREIGN KEY (id_Chambre) REFERENCES Chambre(id_Chambre)
);

CREATE TABLE Offre (
    id_hotel INT,
    id_prestation INT,
    PRIMARY KEY (id_hotel, id_prestation),
    FOREIGN KEY (id_hotel) REFERENCES Hotel(id_hotel),
    FOREIGN KEY (id_prestation) REFERENCES Prestation(id_prestation)
);

