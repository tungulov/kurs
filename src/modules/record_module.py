from typing import List, Optional

from src.connection import DBConnection, db_config, provider


def record_module_get_ships() -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'record_ships.sql',
        )

        cursor.execute(sql_statement)
        
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]

        if len(result) == 0:
            return None

        return result
    

def record_module_add_record(ship_id, employer_id):
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'add_ship_record.sql',
            {"ship_id": ship_id, "employer_id": employer_id}
        )
        cursor.execute(sql_statement)