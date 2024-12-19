DELIMITER $$

CREATE PROCEDURE GetRegistrationCardsByMonthAndYear(IN search_month INT, IN search_year INT)
BEGIN
    SELECT 
        rc.id AS registration_id,
        rc.arrival_date,
        rc.leaving_date,
        ue.name AS employer_name,
        s.ship_name,
        s.tonnage
    FROM 
        Registration_card rc
    JOIN 
        User_EXTERNAL ue ON rc.employer_id = ue.id
    JOIN 
        Ships s ON rc.ship_id = s.id
    WHERE 
        MONTH(rc.arrival_date) = search_month
        AND YEAR(rc.arrival_date) = search_year;
END $$

DELIMITER ;
