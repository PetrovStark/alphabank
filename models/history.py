from datetime import datetime

class History(object):
    def __init__(self):
        self.__transactions = []
    
    def add(self, message):
        formatted_date = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S')
        message = '[{}] - {}'.format(formatted_date, str(message))
        self.__transactions.append(message)
    
    def show(self, order = 'DESC', limit = 10):
        transactions = self.__transactions[:limit]
        if order == 'DESC':
            order_message = 'Last'
            transactions.reverse()
        elif order == 'ASC':
            order_message = 'First'
        
        print('{} {} transactions:'.format(order_message, len(transactions)))
        counter = 0
        for transaction in transactions:
            if limit <= counter:
                break

            print(transaction)
            counter+=1