class Account:
    total_accounts = 0

    def __init__(self, User, amount):
        Account.total_accounts += 1
        self.__id = Account.total_accounts
        self.__User = User
        self.__amount = float(amount)
         
    @property
    def id(self):
        return self.__id
    
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
