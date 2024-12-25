from typing import List, Optional
from src.connection import DBConnection, db_config, provider
from src.common.table_naming import employee_types


def get_workers() -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'all_workers.sql',
        )

        cursor.execute(sql_statement)
        
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]
        
        return result
    

def add_brigade(ship_id: int, selected_employees: List[int]):
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'add_brigade.sql', {
                'ship_id' : ship_id
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


def get_all_brigades_with_ship_and_employees_count():
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'get_all_brigades_with_ship_and_employees_count.sql'
        )
        cursor.execute(sql_statement)

        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]
        
        return result