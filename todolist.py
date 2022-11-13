user_input = 'random'
data = []

def show_menu():
    print("=================================================================")
    print("MENU:")
    print("1. Add an item")
    print("2. Mark as done")
    print("3. View the to do list")
    print("4. Exit")
    print("=================================================================")

while user_input != '4':

    show_menu()
    user_input = input('Enter your choice: ')

    if user_input == "1":
        item = input("What is to be done? ")
        data.append(item)
        print(f"Added item {item}")
    elif user_input == "2":
        item = input("What is to be marked as done? ")
        if item in data:
            data.remove(item)
            print(f"Removed item: {item}")
        else:
            print("Item does not exist in the list")

    elif user_input == "3":
        print("List of all to do items")
        for item in data:
            print(item)
    elif user_input == "4":
        print("Goodbye!")
    else:
        print("Please enter a valid input between 1 and 4")
