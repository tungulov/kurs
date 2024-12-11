SELECT
    id,
    user_group,
    role
FROM internal_user
WHERE 1=1
    AND login='$login'
    AND password='$password'