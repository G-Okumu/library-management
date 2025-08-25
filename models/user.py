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
    
    # Move this to appropriate class
    # Keep it simple for the students also
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
        
        
    @property
    def username(self) -> str:
        return self._username
    
    # just a way of setting username on its own unique way
    @username.setter
    def username(self, value: str):
        unique_username = f"{value.lower()}_{value[0].lower()}"
        self._username = unique_username
        
    # Validating role to be only of type student, admin and librarian
    # add teacher later
    
    @property
    def role(self) -> str:
        return self._role
    
    @role.setter
    def role(self, value: str):
        role = value.lower()
        if role not in ['student', 'admin', 'librarian']:
            raise ValueError(f"Role must be one of student, admin and librarian")
        
        self._role = role
    