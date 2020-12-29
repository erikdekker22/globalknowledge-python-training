def ask_amount():
    '''Asks the user for an amount.

    Prints an error if the amount is smaller that 0 and returns 0.
    Else it will return the amount of the user.'''
    amount = int(input("What is the amount user: "))
    if amount >= 0:
        print("Great! That is exactly what I wanted!")
        return amount
    else:
        print("That is not a positive number!")
        return 0

    return amount

def main():
    amount = ask_amount()
    message = "The user wants " + str(amount)
    print(message)

main()