SELECT 
    B.id AS brigade_id,
    B.work_date,
    S.ship_name,
    B.status,
    S.tonnage,
    COUNT(Be.id) AS employees_count
FROM 
    Brigade B
JOIN 
    Ship S ON B.ship_id = S.id
LEFT JOIN 
    BrigadeEmployees Be ON B.id = Be.brigade_id
GROUP BY 
    B.id, B.work_date, S.ship_name, S.tonnage
ORDER BY
    B.id;
