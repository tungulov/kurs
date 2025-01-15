SELECT 
    Ship.id,
    Ship.ship_name,
    Ship.tonnage,
    Ship.home_port,
    Ship_types.name AS ship_type_name,
    Ship.unloaded_date
FROM 
    Ship
JOIN 
    Ship_types 
ON 
    Ship.ship_type_id = Ship_types.id
WHERE 
    Ship.unloaded_date IS NULL
ORDER BY 
    Ship.id;
