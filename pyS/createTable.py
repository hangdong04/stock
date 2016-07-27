from Service.DBHelper import DBHelper
from DataAccess.StockAccess import StockAccess
from Service.DBConfig import DBConfig

db = DBHelper()
stockAccess = StockAccess(db)
table_string = ", ".join((", ".join(
    [" ".join([key, str(val)]) for key, val in DBConfig.table.items()]),
                          ",".join(DBConfig.constraint)))

for sym in stockAccess.getAllSymbol():
    sql = "CREATE TABLE IF NOT EXISTS `%s` (%s)ENGINE= InnoDB;" % \
                   (sym['symbol'], table_string)
    db.query(sql)