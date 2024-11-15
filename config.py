import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="belajar"
        )
        if connection.is_connected():
            print("Berhasil terhubung ke MySQL")
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None
