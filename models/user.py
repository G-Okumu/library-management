import re
import hashlib

class User():
    def __init__(self, username, password, role):
        self.id = None # auto generated form db
        self.username = username
        self.password = password
        self.role = role
    
    @property
    def password(self)-> str:
        return self._password
    
    ## Move this to appropriate class
    @password.setter
    def password(self, value: str):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long")

        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")

        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")

        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character")
        
        # hash before storing
        self._password = hashlib.sha256(value.encode()).hexdigest()
    