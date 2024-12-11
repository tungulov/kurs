from flask import session

from src.connection import DBConnection, db_config, provider

def auth(login: str, password: str, is_admin_value: bool) -> bool:
    if is_admin_value == 'on': 
        with DBConnection(db_config) as cursor:
            sql_statement = provider.get(
                'find_internal_user.sql',
                {'login': login, 'password': password}
            )

            cursor.execute(sql_statement)
            row = cursor.fetchone()
            
            if row is None: 
                return False
            
            session['user_id'] = row[0]
            session['name'] = row[1]
            session['role'] = row[2]
            session['is_admin'] = True
            session.permanent = True
            return True
        
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'find_external_user.sql',
            {'login': login, 'password': password}
        )

        cursor.execute(sql_statement)
        row = cursor.fetchone()
        if row is None: 
            return False
        

        session['user_id'] = row[0]
        session['name'] = row[1]
        session['is_admin'] = False
        session.permanent = True


    return True
    
