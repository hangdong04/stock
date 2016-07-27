import csv
import urllib2
from Service.DBHelper import DBHelper
from DataAccess.StockAccess import StockAccess
from Model.StockModel import StockModel

data = []
db = DBHelper()
stockAccess = StockAccess(db)


for sym in stockAccess.getAllSymbol():
    url = 'http://real-chart.finance.yahoo.com/table.csv?s='+sym['symbol']
    print sym['symbol']
    try:
        response = urllib2.urlopen(url)
        cr = csv.reader(response)
        keep = False
        for row in cr:
            if keep:
                stockModel = StockModel()
                stockModel.date = row[0]
                stockModel.open = row[1]
                stockModel.high = row[2]
                stockModel.low = row[3]
                stockModel.close = row[4]
                stockModel.volume = row[5]
                data.append(stockModel)
            keep = True
        stockAccess.addData(sym['symbol'], data)
        data = []
    except:
        pass