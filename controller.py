from models.user import User
from models.account import Account


class Controller(object):
    def __init__(self, instanceApp):
        self.App = instanceApp
        self.procedures = {
            'help': {
                'description': 'Shows all the available procedures',
                'method': self.help
            },
            'register': {
                'description': 'Register a new account.',
                'method': self.register
            },
            'login': {
                'description': 'Log in to your account.',
                'method': self.login
            },
            'logout': {
                'description': 'Log out from your account.',
                'method': self.logout
            },
            'deposit': {
                'description': 'Deposit a certain amount in your account.',
                'method':self.deposit
            },
            'withdraw': {
                'description': 'Withdraw a certain amount from your account.',
                'method': self.withdraw
            },
            'transfer': {
                'description': 'Transfer a certain amont to another account.',
                'method': self.transfer
            },
            'extract': {
                'description': 'See your account\'s current status.',
                'method': self.extract
            },
            'history': {
                'description': 'See your account\'s last transactions',
                'method': self.history
            },

            'exit': {
                'description': 'Exit the application.'
            }
        }

    def execute_procedure(self, procedure):
        if (procedure not in self.procedures):
            raise Exception(
                'Procedure not found, please try again. (Type "help" to see all available procedures)')

        self.procedures[procedure]['method']()

    def register(self):
        name = input('Your name: ')
        email = input('Your email:  ')
        password = input('Your password: ')
        user = User(name, email, password)
        user.register(user)
        user.account.history.add('Was created.')

        print('\nWelcome to Alphabank, {}!'.format(user.name))

        return True

    def login(self):
        if (self.App.user != False):
            raise Exception(
                'You are already logged in.\nTo log into another account, you must log out of this one first by typing the "logout" command.')

        email = input('Your e-mail:  ')
        password = input('Your password:  ')
        self.App.user = User.login(email, password)
        self.App.user.account.history.add('Logged in.')
        print('Hi, {}!'.format(self.App.user.name))

    def logout(self):
        self.App.is_authenticated()
        print('Bye, {}!'.format(self.App.user.name))
        self.App.user.account.history.add('Logged out.')
        self.App.user = False

    def deposit(self):
        self.App.is_authenticated()
        amount = input('Type the amount in U$ Dollars:  ')
        self.App.user.account.deposit(amount)
        feedback = 'You successfully deposited ${} to your account.'.format(
            amount)
        self.App.user.account.history.add(feedback)
        print(feedback)

    def withdraw(self):
        self.App.is_authenticated()
        amount = input('Type the amount in U$ Dollars:  ')
        self.App.user.account.withdraw(amount)
        feedback = 'You successfully withdrew ${} from your account.'.format(
            amount)
        self.App.user.account.history.add(feedback)
        print(feedback)

    def extract(self):
        self.App.is_authenticated()
        self.App.user.account.extract()
        self.App.user.account.history.add('Consulted your account\'s extract.')

    def history(self):
        self.App.is_authenticated()
        self.App.user.account.history.show()
        self.App.user.account.history.add('Consulted your account\'s history.')

    def transfer(self):
        self.App.is_authenticated()
        accountId = int(input('Type the destiny account ID:  '))
        amount = float(input('Type the amount in U$ Dollars:  '))
        
        self.App.user.account.transfer(amount, accountId)

    def help(self):
        procedures = [func for func in dir(Controller) if callable(
            getattr(Controller, func)) and not func.startswith("_")]
        # Adding the exit procedure, which not has a method.
        procedures.remove('execute_procedure')

        for procedure in procedures:
            procedure_show = '\n"{}"'.format(str(procedure))

            if 'description' in self.procedures[procedure] :
                procedure_show += " - {}".format(self.procedures[procedure]['description'])
            
            print(procedure_show)