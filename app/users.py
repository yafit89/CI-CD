import requests

def get_users() -> list:
    response = requests.get('https://dummyjson.com/users?limit=100')
    users = response.json().get('users', [])

    return users


def print_users(users: list) -> None:
    for user in users:
        print(user['firstName'], user['lastName'])


def main():
    users = get_users()
    print_users(users)


if __name__ == '__main__':
    main()

