class Account:
    total_accounts = 0

    def __init__(self, Client, amount):
        Account.total_accounts += 1
        self.__id = Account.total_accounts
        self.__Client = Client
        self.__amount = amount
         
    @property
    def id(self):
        return self.__id
