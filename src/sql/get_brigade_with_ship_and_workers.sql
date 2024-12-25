SELECT 
    B.id AS brigade_id,
    B.work_date,
    B.status,
    S.ship_name,
    S.tonnage,
    S.home_port,
    E.id AS employee_id,
    E.hours,
    U.id AS employer_id,
    U.fio AS employer_name,
    U.profession AS employer_profession
FROM 
    Brigade B
JOIN 
    Ship S ON B.ship_id = S.id
LEFT JOIN 
    BrigadeEmployees E ON B.id = E.brigade_id
LEFT JOIN 
    User U ON E.employer_id = U.id
WHERE 
    B.id = $id;
