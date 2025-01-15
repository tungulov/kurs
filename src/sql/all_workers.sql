SELECT u.id, u.fio, u.employees_date
FROM User u
WHERE u.role = 'employee'
  AND NOT EXISTS (
    SELECT 1
    FROM BrigadeEmployees be
    JOIN Brigade b ON be.brigade_id = b.id
    WHERE be.employer_id = u.id
      AND b.work_date = '$date_created'  -- Указываем дату, на которую ищем свободных работников
  )
ORDER BY u.id;
