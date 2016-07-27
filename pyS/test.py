import datetime
from Service.DBHelper import DBHelper
from DataAccess.StockAccess import StockAccess
from Model.StockModel import StockModel
from yahoo_finance import Share

data_list = []
db = DBHelper()
stockAccess = StockAccess(db)


now = datetime.datetime.now()
time_form = "%Y-%m-%d"
recent_date = now.strftime(time_form)

for sym in stockAccess.getAllSymbol():
    prev = str(stockAccess.getLastDate(sym['symbol'])[0]["date"])
    a = datetime.datetime.strptime(prev, time_form)
    b = now
    if b > a:
        stock = Share(sym['symbol'])
        stock_list = stock.get_historical(prev, recent_date)
        for data in stock_list:
            stockModel = StockModel()
            stockModel.date = data['Date']
            stockModel.date = data['Open']
            stockModel.date = data['High']
            stockModel.date = data['Low']
            stockModel.date = data['Close']
            stockModel.date = data['Volume']
            data_list.append(stockModel)
        stockAccess.addData(sym['symbol'], data_list)
        data_list = []
