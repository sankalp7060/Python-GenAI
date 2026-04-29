class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def verify_password(self, input_password):
        return self.__password == input_password


u = User("Alex", "secure123")
print(u.verify_password("secure123"))