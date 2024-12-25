SELECT
    *
FROM User
WHERE 1=1
    AND name='$login'
    AND password='$password'
    AND fired_date IS NULL