SELECT 
    Ship.id,
    Ship.ship_name,
    Ship.tonnage,
    Ship.home_port,
    Ship.ship_type_id,
    Ship_types.name AS ship_type_name
FROM 
    Ship
JOIN 
    Ship_types 
ON 
    Ship.ship_type_id = Ship_types.id
WHERE
    Ship.id = $id;
