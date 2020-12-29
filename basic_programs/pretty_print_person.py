def pretty_print_person(first_name, last_name):
    print('Voornaam : ' + first_name)
    print('Achternaam : ' + last_name)


def main():
    f_name = "Guido"
    l_name = "van Rossum"
    pretty_print_person(f_name, l_name)


if __name__ == "__main__":
    main()