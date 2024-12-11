from src.connection import DBConnection

def find_user_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()

    if row is None: 
        return None
    
    return {
        'user_id': row[0],
        'user_group': row[1],
        'role' : row[2]
    }
