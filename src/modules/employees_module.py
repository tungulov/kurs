from typing import List, Optional
from src.connection import DBConnection, db_config, provider
from src.common.table_naming import employee_types


def get_employees() -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'all_employees.sql',
        )

        cursor.execute(sql_statement)
        
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]
        
        return result
    

def get_employee(employee_id) -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'find_employee.sql', {'id' : employee_id}
        )
        cursor.execute(sql_statement)
        return cursor.fetchone()
    

def add_employee(fio, name, password, employee_type):
    for type in employee_types:
        if employee_types[type] == employee_type:
           profession = type

    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'add_employee.sql',
            {
                'name' : name,
                'password' : password,
                'fio' : fio,
                'profession' : profession,
                'role' : employee_type,   
            }
        )
        cursor.execute(sql_statement)


def edit_employee(id, fio, name, password, employee_type, restore_employee):
    for type in employee_types:
        if employee_types[type] == employee_type:
           profession = type

    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'edit_employee.sql',
            {   
                'id' : id,
                'name' : name,
                'password' : password,
                'fio' : fio,
                'profession' : profession,
                'role' : employee_type,   
            }
        )
        cursor.execute(sql_statement)

        if restore_employee == 'on':
            sql_statement = provider.get(
                'restore_employee.sql',
                {
                    'id' : id,
                }
            )
            cursor.execute(sql_statement)
    

def delete_employee(employee_id):
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'delete_employee.sql',
            {
                'employee_id' : employee_id
            }
        )

        cursor.execute(sql_statement)
