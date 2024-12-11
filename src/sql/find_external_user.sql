SELECT
    id,
    name
FROM User_EXTERNAL
WHERE 1=1
    AND name='$login'
    AND password='$password'