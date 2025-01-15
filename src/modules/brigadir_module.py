from typing import List, Optional
from src.connection import DBConnection, db_config, provider
from src.common.table_naming import employee_types


def get_workers(date_created) -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'all_workers.sql',{
                'date_created' : date_created
            }
        )

        cursor.execute(sql_statement)
        
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]
        
        return result
    

def add_brigade(ship_id: int, selected_employees: List[int], date_created):
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'add_brigade.sql', {
                'ship_id' : ship_id,
                'date_created' : date_created
            }
        )
        cursor.execute(sql_statement)
        brigade_id = cursor.lastrowid

        for employee_id in selected_employees:
            sql_statement = provider.get(
                'add_brigade_employers.sql', {
                    'brigade_id' : brigade_id,
                    'employer_id' : employee_id
                }
            )
            cursor.execute(sql_statement)

        sql_statement = provider.get(
            'set_ship_date_created.sql', {
                'ship_id' : ship_id,
                'date_created' : date_created
            }
        )
        cursor.execute(sql_statement)

def get_all_brigades_with_ship_and_employees_count():
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'get_all_brigades_with_ship_and_employees_count.sql'
        )
        cursor.execute(sql_statement)

        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]
        
        return result
    

def get_brigade_with_ship_and_workers(brigade_id: int):
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'get_brigade_with_ship_and_workers.sql', {
                'id' : brigade_id
            }
        )
        cursor.execute(sql_statement)

        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]
        
        return result
    

def set_brigade_data(brigade_id: int, selected_brigade_employers: List, status: str):
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'edit_brigade_status.sql', {
                'id' : brigade_id,
                'status' : status
            }
        )
        cursor.execute(sql_statement)

        for brigade_employee in selected_brigade_employers:
            sql_statement = provider.get(
                'edit_birgade_employee_hour.sql', {
                    'id' : brigade_employee[0],
                    'hours' : brigade_employee[1]
                }
            )
            cursor.execute(sql_statement)
