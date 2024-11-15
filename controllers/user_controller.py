from viewmodels.user_viewmodel import UserViewModel
from models.user_model import UserModel

class UserController:
    @staticmethod
    def fetch_user(user_id):
        view_model = UserViewModel(user_id)
        return view_model.get_user_data()

    @staticmethod
    def create_user(name, email):
        return UserModel.create_user(name, email)

    @staticmethod
    def update_user(user_id, name, email):
        return UserModel.update_user(user_id, name, email)

    @staticmethod
    def delete_user(user_id):
        return UserModel.delete_user(user_id)
