from typing import List, Optional
from src.connection import DBConnection, db_config, provider


def call_procedure(db_config, sql):
    with DBConnection(db_config) as cursor:
        cursor.execute(sql)
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]

        return {
            'status': True if result else False,
            'ships': result
        }

def get_ships() -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'ships_with_types.sql',
        )

        cursor.execute(sql_statement)
        
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]
        
        return result
    

def get_unloaded_ships(date_created) -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'unloaded_ships_with_types.sql', {
                  'date_created' : date_created
            }
        )

        cursor.execute(sql_statement)
        
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]
        
        return result
    

def get_ship(ship_id) -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'find_ship_with_types.sql', {'id' : ship_id}
        )
        cursor.execute(sql_statement)
        return cursor.fetchone()
    

def delete_ship(ship_id) -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'delete_ship.sql', {'ship_id' : ship_id}
        )
        cursor.execute(sql_statement)

def add_ship(ship_name, tonnage, home_port, ship_type_id):
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'add_ship.sql', {
                "ship_name" : ship_name,
                "tonnage" : tonnage,
                "home_port" : home_port,
                "ship_type_id" : ship_type_id
            }
        )
        cursor.execute(sql_statement)


def edit_ship(ship_id, ship_name, tonnage, home_port, ship_type_id):
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'edit_ship.sql', {
                'ship_id' : ship_id,
                "ship_name" : ship_name,
                "tonnage" : tonnage,
                "home_port" : home_port,
                "ship_type_id" : ship_type_id
            }
        )
        cursor.execute(sql_statement)


def get_ships_types() -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'all_ship_types.sql',
        )
        cursor.execute(sql_statement)
        return cursor.fetchall()