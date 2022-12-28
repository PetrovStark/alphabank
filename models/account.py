import locale
from models.history import History


class Account:
    __accounts = []

    def __init__(self, User, amount):
        self.__id = len(Account.__accounts) + 1
        self.__User = User
        self.__amount = float(amount)
        self.__History = History()

        Account.__accounts.append({
            'id': self.__id,
            'instance': self
        })

    @staticmethod
    def get(id):
        for account in Account.__accounts:
            if account['id'] != id:
                continue
            
            return account['instance']
        
        raise Exception(
            'Account not found.')

    @property
    def id(self):
        return self.__id

    @property
    def history(self):
        return self.__History
    
    @property
    def user(self):
        return self.__User
    
    def extract(self):
        print('Account ID: {}'.format(self.__id))
        print('Owner: {}'.format(self.__User.name))
        print('Actual amount: {}'.format(self.__format_amount(self.__amount)))
        self.__History.show(limit=5)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise Exception(
                'Transaction not authorized, you can only deposit values greater than US$0')

        self.__amount += amount
        return True

    def withdraw(self, amount):
        amount = float(amount)
        if self.__amount - amount < 0:
            raise Exception(
                'Transaction not authorized, insufficient funds.')

        if amount <= 0:
            raise Exception(
                'Transaction not authorized, you can only withdraw values greater than US$0')

        self.__amount -= amount
        return True
    
    def transfer(self, amount, accountId):
        destiny = False
        withdrew = False
        deposited = False

        try:
            destiny = Account.get(accountId)
            if destiny.id == self.id:
                raise Exception('You cannot transfer money to your own account.')
            
            withdrew = self.withdraw(amount)
            deposited = destiny.deposit(amount)

            self.history.add(
                'Transferred ${} to "{}" (Account ID: {}).'.format(
                    amount,
                    destiny.user.name,
                    destiny.id))
            
            destiny.history.add(
                'Received ${} from "{}" (Account ID: {}).'.format(
                    amount,
                    self.user.name,
                    self.id))

        except Exception as e:
            if bool(deposited):
                destiny.withdraw(amount)

            if bool(withdrew):
                self.deposit(amount)
            
            if bool(destiny):
                self.history.add(
                    'Tried to transfer ${} to "{}" (Account ID: {}), but failed due to this error: {}'.format(
                        amount,
                        destiny.user.name,
                        destiny.id,
                        str(e)))
            else :
                self.history.add(
                    'Tried to transfer ${}, but destiny account was not found.'.format(amount))

            raise Exception(
                'Transference error: {}'.format(str(e)))

    @staticmethod
    def __format_amount(amount):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
        return locale.currency(amount)
