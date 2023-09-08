import mysql.connector
class DatabaseConnection:
    _connection = None
    @classmethod
    def get_connection(cls, db_name):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
            host='127.0.0.1',
            user='juan',
            port = "3306",
            password='123456',
            database= db_name
            )
        return cls._connection
    
    @classmethod
    def execute_query(cls, query, params=None, db_name = None):
        cursor = cls.get_connection(db_name).cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        return cursor
    @classmethod
    def fetch_one(cls, query, params=None, db_name = None):
        cursor = cls.get_connection(db_name).cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
    @classmethod
    def fetch_all(cls, query, params=None, db_name = None):
        cursor = cls.get_connection(db_name).cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
