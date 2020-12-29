from random import randint

def ask_min_max_numbers():
    max_value = int(input("Please specify a maximum value: ")) # ask for max value
    min_value = int(input("Please specify a minimum value: ")) # ask for min value

    while min_value >= max_value: # loop till you enter a min value that is less than the max value
        print("You are stuck in my loop! If you want to get out, please specify a lower value than you maximum value: ")
        min_value = int(input("Please specify a new minimum value: "))
    else:
        print("Fine you are free. You had given the max value of " + str(max_value) + " and a min value of " + str(min_value) + '.')
        return min_value, max_value



def select_random_number(min, max):
    '''Start een oneindige loop waarin je een random getal genereert tussen min en max.
    Toon het nummer en vraag of dit getal geselcteerd moet worden
    Indien de gebruiker 'yes' ingeeft, retourneer je het getal.
    In alle andere gevallen zeg je dat je een een nieuw getal gaat maken en je blijft in de loop.
    '''
    chosen_one = randint(min, max)
    print("Dear user. You have been provided the number **" + str(chosen_one) + "**. Are you satisfied? Or do you want another one?")
    answer = input("Please Type \"Yes\" or \"No\".").upper()

    while answer != "YES":
        chosen_one = randint(min, max)
        print("You have been assigned a new number **" + str(chosen_one) + "**. Are you satisfied? Or do you want another one?")
        answer = input("Please Type \"Yes\" or \"No\".").upper()
    else:
        return chosen_one


def main():
    min, max = ask_min_max_numbers()
    number = select_random_number(min, max)

    message = ("Great! You have finally chosen **" + str(number) + "**.")
    print(message)


if __name__ == "__main__":
    main()