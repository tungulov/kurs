UPDATE Ship
SET ship_name = '$ship_name', tonnage = $tonnage, home_port = '$home_port', ship_type_id = $ship_type_id
WHERE id = $ship_id;
