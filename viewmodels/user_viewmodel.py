from models.user_model import UserModel

class UserViewModel:
    def __init__(self, user_id):
        self.user = UserModel.get_user(user_id)

    def get_user_data(self):
        if self.user:
            return {
                "user_id": self.user.user_id,
                "name": self.user.name,
                "email": self.user.email
            }
        return None
