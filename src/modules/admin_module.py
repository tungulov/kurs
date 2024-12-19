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
    
def get_ship_types():
    with DBConnection(db_config) as cursor:
        sql_statement = provider.get(
            'all_ship_types.sql',
        )
        cursor.execute(sql_statement)
        row = cursor.fetchall()