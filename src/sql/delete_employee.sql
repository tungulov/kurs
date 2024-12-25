UPDATE User
SET fired_date = CURRENT_DATE
WHERE id = $employee_id;
