from Service.DBConfig import DBConfig
class StockAccess:
    def __init__(self, db):
        self.__db = db
        self.__config = DBConfig

    def addSymbol(self, symbol):
        sql = "INSERT INTO stock (symbol) VALUES ('%s')" % (symbol)
        result = self.__db.query(sql)
        return result

    def getAllSymbol(self):
        sql = ("select * from stock")
        result = self.__db.select(sql)
        return result

    def createTable(self, name):
        table_string = ", ".join((", ".join([" ".join([key, str(val)]) for key, val in self.__config.table.items()]), ",".join(self.__config.constraint)))
        create_table = "CREATE TABLE %s (%s)ENGINE= InnoDB" % \
                               (name, table_string)
        result = self.__db.query(create_table)
        return result

    def addData(self, symbol, data):
        for stockModel in data:
            sql = "INSERT INTO `%s` (date, open, high, low, close, volume) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
            symbol, stockModel.date, stockModel.open, stockModel.high, stockModel.low, stockModel.close, stockModel.volume)
            result = self.__db.query(sql)
        return result
    def getLastDate(self, symbol):
        sql = 'SELECT date FROM `%s` ORDER BY date DESC LIMIT 1;' % (symbol)
        result = self.__db.select(sql)
        return result



