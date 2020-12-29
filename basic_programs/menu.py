import sys

def load_confuration():
    print("Loading configuration")

def save_configuration():
    print("Saving confuration")

def quitting():
    print("Quiting")

def what_to_do(value):
    # value = input("What to do? [load, save, quit] ") # --> could be done instead of sys.argv
    if value == 'load': # is the value equal to load?
        load_confuration()
    elif value == 'save': # is the value equal to save?
        save_configuration()
    elif value == 'quit': # is the value equal to quit?
        quitting()
    else: # in all other cases
        print("This is highly unsual!? This was not one of the options you could give. ")

def main():
    what_to_do(sys.argv[1]) # give the python file an argument on the terminal, e.g., "menu.py quit" or "menu.py save"

main()