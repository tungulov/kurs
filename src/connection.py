from pymysql import connect
import os
from pymysql.err import OperationalError

from src.sql_provider import SqlProvider


db_host = 'mysql_db' if os.getenv('PROD') == "True" else '127.0.0.1'

db_config = {
    'host': db_host,
    'port': int(os.getenv('MYSQL_ROOT_PORT')),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_ROOT_PASSWORD'),
    'db': os.getenv('MYSQL_DATABASE')
}

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

class DBConnection:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = connect(**self.db_config)
            self.cursor = self.connection.cursor()
            return self.cursor
        except RuntimeError as err:
            print('error:', err)
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection and self.cursor:
            if exc_type:
                print('exc type:', exc_type)
                print('exc value:', exc_val)
                self.connection.rollback()
            else:
                self.connection.commit()
            self.cursor.close()
            self.connection.close()
        else:
            if exc_type:
                print('exc type:', exc_type)
                print('exc value:', exc_val)
        return True
