import locale
from models.history import History
class Account:
    total_accounts = 0

    def __init__(self, User, amount):
        Account.total_accounts += 1
        self.__id = Account.total_accounts
        self.__User = User
        self.__amount = float(amount)
        self.__History = History()
         
    @property
    def id(self):
        return self.__id
    
    @property
    def history(self):
        return self.__History
    
    def extract(self):
        return 'Actual amount: {}'.format(self.__format_amount(self.__amount))
    
    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise Exception('Transaction not authorized, you can only deposit values greater than US$0')

        self.__amount += amount
    
    def withdraw(self, amount):
        amount = float(amount)
        if self.__amount - amount < 0:
            raise Exception('Transaction not authorized, insufficient funds.')
        
        if amount <= 0:
            raise Exception('Transaction not authorized, you can only withdraw values greater than US$0')
        
        self.__amount -= amount
    
    @staticmethod
    def __format_amount(amount):
        locale.setlocale( locale.LC_ALL, 'en_US.utf-8' )
        return locale.currency(amount)
