from repositories.user_repository import UserRepository

class UserService():
    def add_user(user):
        UserRepository.create_user(user)
        print(f"Thank you, you've just created {user.role}")