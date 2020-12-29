import sys


def ask_username():
    username = input("please type your username: ").strip()
    if ('    ' in username ) or (' ' in username):
        print("Your username may not contain tabs or spaces")
        sys.exit(42)
    elif len(username) <= 3:
        print("Your username is to short!")
        sys.exit(1)
    else:
        return username


def ask_password(username):
    password = input("please type your password: ")
    if len(password) <= 5:
        print("Your password is to short!")
        sys.exit(46)
    elif password == username:
        print("Password and username cannot be the same! ")
        sys.exit(45)
    else:
        return password


def is_welcome(name, passwd):
    if (name != None) and (passwd != None):
        return True  # fixture, replace


def main():
    username = ask_username()
    password = ask_password(username)

    if is_welcome(username, password):
        message = "Welcome in " + username + "."
        print(message)
    else:
        message = "Not allowed."
        print(message)
    sys.exit(0)


if __name__ == "__main__":
    main()