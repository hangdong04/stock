class StockModel:
    def __init__(self):
        self.__volume = None
        self.__close = None
        self.__high = None
        self.__low = None
        self.__open = None
        self.__date = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def close(self):
        return self.__close

    @close.setter
    def close(self, value):
        self.__close = value

    @property
    def high(self):
        return self.__high

    @high.setter
    def high(self, value):
        self.__high = value

    @property
    def low(self):
        return self.__low

    @low.setter
    def low(self, value):
        self.__low = value

    @property
    def open(self):
        return  self.__open

    @open.setter
    def open(self, value):
        self.__open = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

