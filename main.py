to_do_file = open("files/todo-data.txt", "r")
to_do_list = []
for line in to_do_file:
    line = line.strip()
    line = line.strip("\n")
    to_do_list.append(line)
to_do_file.close()
print("Welcome, your current list is: ")
for index, to_do in enumerate(to_do_list):
    print(f"{index + 1}. {to_do}")
print("Welcome to the to do application!")
while True:
    to_do_action = input("Would you like to leave the application or add, edit, show, complete, or delete an item: ")\
        .strip()
    to_do_action = to_do_action.lower().strip()

    match to_do_action:
        case 'add':
            to_do_item = input("Type the name of the item: ").strip()
            to_do_list.append(to_do_item)
            to_do_file = open(r"files\todo-data.txt", "w")
        case "show" | "display":
            print("Displaying items.")
            for index, to_do in enumerate(to_do_list):
                print(f"{index + 1}. {to_do}")
        case "delete" | "remove":
            delete_index = input("What item would you like to delete: ").strip()
            if delete_index.isdigit():
                delete_index = int(delete_index) - 1
            else:
                print("Error, not an index.")
                continue
            if len(to_do_list) > delete_index > -1:
                print(f"Successfully deleted {to_do_list.pop(delete_index)}")
            else:
                print("Item does not exist.")
        case "finish" | "complete":
            complete_name = input("Which item have you completed: ").strip()
            if to_do_list.__contains__(complete_name):
                to_do_list.remove(complete_name)
                print(f"Congratulations for finishing {complete_name}!")
            else:
                print("That item doesn't exist. Guess it's already done then?")
        case "edit":
            number = input("Number of item to edit: ").strip()
            if number.isdigit():
                number = int(number) - 1
            else:
                print("Error, not an index.")
                continue
            if len(to_do_list) > number > -1:
                to_do_list[number] = input("Enter replacement item: ")
            else:
                print("Error, that item isn't being tracked!")
        case "end":
            break
        case default:
            print("Invalid input!")
    to_do_file = open("files/todo-data.txt", "w")
    #Write all changes to file, if any.
    for to_do in to_do_list:
        to_do_file.write(f"{to_do}\n")
    to_do_file.close()
print("Thank you for using the to do tracker application!")
