import mysql.connector
import os
import requests


def get_users() -> list:
    response = requests.get('https://dummyjson.com/users?limit=3')
    users = response.json().get('users', [])
    return users


def mysql_connection() -> mysql.connector.connection.MySQLConnection:
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "test_db")
    )
    return connection


def insert_users(users: list) -> None:
    cursor.execute("TRUNCATE TABLE users")

    for user in users:
        cursor.execute(
            "INSERT INTO users (id, name) VALUES (%s, %s)",
            (user['id'], f"{user['firstName']} {user['lastName']}")
        )
        print(f"User {user['firstName']} {user['lastName']} inserted successfully!")

    connection.commit()
    cursor.close()
    connection.close()
    print("##### Users inserted successfully! #####")


def check_data():
    print("##### Checking data in DB #####")
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users


if __name__ == "__main__":
    action = os.getenv("ACTION", "write")

    global connection, cursor
    connection = mysql_connection()
    cursor = connection.cursor()

    if action == "write":
        users = get_users()
        insert_users(users)
    elif action == "check":
        users = check_data()
        print(f"Users in DB: {users}")
