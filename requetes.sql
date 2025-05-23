USE projet_bdr;

SELECT DISTINCT R.id_reservation, R.Date_d_arrivee, R.Date_depart, C.Nom_complet, H.Ville
FROM Reservation R
JOIN Client C ON R.Nom_complet = C.Nom_complet
JOIN Concerner Co ON Co.id_reservation = R.id_reservation
JOIN Chambre Ch ON Ch.id_Chambre = Co.id_Chambre
JOIN Hotel H ON E.id_Hotel = H.id_Hotel;

SELECT *
FROM Client
WHERE Ville = 'Paris';


SELECT Nom_complet, COUNT(*) AS nb_reservations
FROM Reservation
GROUP BY Nom_complet;



SELECT TC.type_chambre, COUNT(*) AS nb_chambres
FROM Chambre C
JOIN Type_Chambre TC ON C.id_type = TC.id_type
GROUP BY TC.type_chambre;


SELECT *
FROM Chambre
WHERE id_Chambre NOT IN (
  SELECT id_Chambre
  FROM Reservation
  WHERE Date_d_arrivee < '2025-06-15'
  AND Date_depart >'2025-07-15'
  )
LIMIT 0, 25;


