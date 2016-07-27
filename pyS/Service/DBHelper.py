import mysql.connector
from mysql.connector import errorcode
from Service.DBConfig import DBConfig


class DBHelper:

    def __init__(self):
        self.config = DBConfig.DB_CONNECT
        self.db_name = DBConfig.DB_NAME
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor(dictionary=True)
        self.set_database(self.db_name)

    def __del__(self):
        self.cursor.close()
        self.cnx.close()

    def set_database(self, db_name):
        try:
            self.cnx.database = db_name
            return 'success'
        except mysql.connector.Error as err:
            return err.msg

    def select(self, sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(err.msg)

    def query(self, sql):
        try:
            self.cursor.execute(sql)
            self.commit()
            return 'success'
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                return 'success'
            print(err.msg)

    def commit(self):
        try:
            self.cnx.commit()
        except mysql.connector.Error as err:
            print(err.msg)
