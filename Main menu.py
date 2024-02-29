menu_options = {
    1: 'Say your Cool',
    2: 'Add a Student',
    3: 'Look Up Student Record',
    4: 'Exit/Quit'
}

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

while True:
    print_menu()
    option = input("What would you like to do? ")

    if option == '1':
        print("\nYour Cool")
    elif option == '2':
        print("\nStudent Added")
    elif option == '3':
        print("\nStudents arn't real")
    elif option == '4':
        print("\nGoodbye")
        break
    else:
        print("\nNot a valid choice. Try again.")
