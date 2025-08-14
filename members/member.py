class Member():
    
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        
    def get_details(self):
        return f"Member name is {self.name} (ID: {self.member_id})"