import csv
from DataAccess.StockAccess import StockAccess
from Service.DBHelper import DBHelper
path = 'C:\Users\Phatthanapong\Desktop\pyS\list.csv'

db = DBHelper()
stockAccess = StockAccess(db)
with open(path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sym = row['Symbol'] + '.bk'
        stockAccess.addSymbol(sym)