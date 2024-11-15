from config import create_connection

class UserModel:
    def __init__(self, user_id=None, name=None, email=None):
        self.user_id = user_id
        self.name = name
        self.email = email

    @staticmethod
    def create_user(name, email):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(query, (name, email))
            connection.commit()
            connection.close()
            return cursor.lastrowid

    @staticmethod
    def get_user(user_id):
        connection = create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            connection.close()
            if result:
                return UserModel(result["user_id"], result["name"], result["email"])
            return None

    @staticmethod
    def update_user(user_id, name, email):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "UPDATE users SET name = %s, email = %s WHERE user_id = %s"
            cursor.execute(query, (name, email, user_id))
            connection.commit()
            connection.close()
            return cursor.rowcount > 0

    @staticmethod
    def delete_user(user_id):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            connection.commit()
            connection.close()
            return cursor.rowcount > 0
