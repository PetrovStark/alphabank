from account import Account
from client import Client
from database import Database

class App:

    def __init__(self):
        self.Client = False
        self.Account = False
        self.Database = Database()
        self.logged_user = False
        self.user_wants_to_exit = False

    def run(self):
        print('Welcome to AlphaBank.')
        print('Type "help" to see all available procedures')
        while (not self.user_wants_to_exit):
            procedure = input('\n$  ')
            if procedure == 'help':
                App.help()

            elif procedure == 'register':
                self.register()
            
            elif procedure == 'login':
                self.login()

            elif procedure == 'exit':
                self.user_wants_to_exit = True

            else :
                print('Procedure not found, please try again. (Type "help" to see all available procedures)')
    
    def register(self):
        name = input('Your name: ')
        email = input('Your email:  ')
        password = input('Your password: ')
        client = Client(name)

        self.Database.register_user(client, Account(client, 0), email, password)

        print('\nWelcome to Alphabank, {}'.format(client.name))
        
        return True
    
    def login(self):
        email = input('Your e-mail:  ')
        password = input('Your password:  ')

        try :
            self.logged_user = self.Database.get_user(email, password)
            print('Welcome, {}'.format(self.logged_user['client'].name))
        
        except Exception as e:
            print(e)

    @staticmethod
    def help():
        procedures = [func for func in dir(App) if callable(getattr(App, func)) and not func.startswith("__")]
        procedures.remove('run') # Removing the method responsible for running the application.
        procedures.append('exit') # Adding the exit procedure, which not has a method.
        print(procedures)

App().run()