from typing import List, Optional
from src.connection import DBConnection, db_config, provider
from src.common.table_naming import employee_types


def employee_statistic(month: int, year: int) -> Optional[List]:
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'use_employee_statistic_procedure.sql', {
                'month' : month,
                'year' : year
            }
        )

        cursor.execute(sql_statement)
        
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema,row)) for row in cursor.fetchall()]
        
        return result