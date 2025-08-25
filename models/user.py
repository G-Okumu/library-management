class User():
    def __init__(self, username, password, role):
        self.id = None # auto generated form db
        self.username = username
        self.password = password
        self.role = role
    