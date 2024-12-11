DELIMITER //

CREATE PROCEDURE GetShipsByMonthYear(
    IN p_month INT,
    IN p_year INT
)
BEGIN
    SELECT 
        id,
        ship_name,
        tonnage,
        home_port,
        ship_type,
        date
    FROM 
        Ships
    WHERE 
        MONTH(date) = p_month AND YEAR(date) = p_year;
END //

DELIMITER ;