SELECT
    id,
    name,
    role
FROM User_INTERNAL
WHERE 1=1
    AND name='$login'
    AND password='$password'