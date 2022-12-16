class Database:
    def __init__(self):
        self.__users = []
    
    @property
    def users(self):
        return self.__users

    def get_user(self, email, password):
        for user in self.__users:
            if user['email'] != email:
                continue
            elif user['password'] == password:
                return user
            
        raise Exception("Invalid email or password.")

    def register_user(self, client_memory_address, account_memory_address, email, password):
        self.__users.append({
            'client': client_memory_address,
            'account': account_memory_address,
            'email': email,
            'password': password
        })