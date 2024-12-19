from flask import session

from src.connection import DBConnection, db_config, provider

def auth_module(login: str, password: str) -> bool:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'find_user.sql',
            {'login': login, 'password': password}
        )

        cursor.execute(sql_statement)
        row = cursor.fetchone()
        if row is None: 
            return False
        
        session['user_id'] = row[0]
        session['name'] = row[1]
        session['role'] = row[6]
        session.permanent = True

    return True
    
