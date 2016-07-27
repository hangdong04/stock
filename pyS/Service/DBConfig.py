class DBConfig():
    DB_CONNECT = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'port': '3306'
    }
    DB_NAME = 'stock'
    KEY_CLOSE = 'close'
    KEY_HIGH = 'high'
    KEY_LOW = 'low'
    KEY_OPEN = 'open'
    KEY_DATE = 'date'
    KEY_VOLUME = 'volume'

    table = {
        KEY_CLOSE: 'TEXT',
        KEY_HIGH: 'TEXT',
        KEY_LOW: 'TEXT',
        KEY_OPEN: 'TEXT',
        KEY_DATE: 'DATE',
        KEY_VOLUME: 'TEXT'
    }
    constraint = ['PRIMARY KEY (%s)' % KEY_DATE]