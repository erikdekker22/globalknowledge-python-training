import sys

def load_confuration():
    print("Loading configuration")

def save_configuration():
    print("Saving confuration")

def quitting():
    print("Quiting")

def what_to_do(value):
    # value = input("What to do? [load, save, quit] ")
    if value == 'load':
        load_confuration()
    elif value == 'save':
        save_configuration()
    elif value == 'quit':
        quitting()
    else:
        print("This is highly unsual")

def main():
    what_to_do(sys.argv[1])

main()