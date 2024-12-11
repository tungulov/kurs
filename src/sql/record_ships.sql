SELECT 
    Ships.id,
    Ships.ship_name,
    Ships.tonnage,
    Ships.home_port,
    Ship_types.name AS ship_type_name
FROM 
    Ships
JOIN 
    Ship_types 
ON 
    Ships.ship_type_id = Ship_types.id;
