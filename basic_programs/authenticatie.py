import sys

def ask_username():
    username = input("please type your username: ").strip()
    if ('    ' in username ) or (' ' in username): # provide error if there are spaces or tabs in username
        print("Your username may not contain tabs or spaces")
        sys.exit(42)
    elif len(username) <= 3: # provide error if username is equal or less than 3 characters
        print("Your username is to short!")
        sys.exit(1)
    else: # else it is OK
        return username

def ask_password(username):
    password = input("please type your password: ")
    if len(password) <= 5: # provide error if password is equal or less than 5 characters
        print("Your password is to short!")
        sys.exit(46)
    elif password == username: # Provide error when the password and username are the same
        print("Password and username cannot be the same! ")
        sys.exit(45)
    else: # else it is OK
        return password

def is_welcome(name, passwd):
    if (name != None) and (passwd != None): # if it passed the previous tests it is oke, thus if both values are not None
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