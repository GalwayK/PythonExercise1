def write_to_do_list(filepath, to_do_list_local):
    with open(filepath, "w") as file:
        [file.write(f"{line}\n") for line in to_do_list_local]
    return None


def read_to_do_list(filepath):
    with open(filepath, "r") as file:
        to_do_list_local = file.readlines()
    return [line.strip().strip("\n") for line in to_do_list_local]


def show_to_do_list(to_do_list_local):
    for index, to_do in enumerate(to_do_list):
        print(f"{index + 1}. {to_do}")


to_do_list = read_to_do_list("files/todo-data.txt")

print("Welcome, your current list is: ")
show_to_do_list(to_do_list)
print("Welcome to the to do application!")

while True:
    to_do_action = input("Would you like to leave the application or add, edit, show, finish, or delete an item: ") \
        .strip()
    to_do_action = to_do_action.strip().strip("\n")

    if to_do_action.lower() == 'add':
        to_do_item = input("Type the name of the item: ").strip()
        to_do_list.append(to_do_item)

    elif to_do_action.lower() == "show" or to_do_action.lower() == "display":
        if len(to_do_list) == 0:
            print("There's nothing to display.")
            continue
        print("Displaying items.")
        show_to_do_list(to_do_list)
        continue

    elif to_do_action.lower() == "delete" or to_do_action.lower() == "remove":
        if len(to_do_list) == 0:
            print("There are no items to delete.")
            continue
        try:
            delete_index = input("What item would you like to delete: ").strip()
            delete_index = int(delete_index) - 1

            removed_item = to_do_list.pop(delete_index)
            print(f"Successfully deleted {removed_item}")

        except ValueError:
            print("Error, invalid input.")
            continue
        except IndexError:
            print("Error, item does not exist.")

    elif to_do_action.lower() == "finish" or to_do_action.lower() == "complete":
        if len(to_do_list) == 0:
            print("There are no items to finish.")
            continue
        try:
            complete_name = input("Which item have you completed: ").strip()
            to_do_list.remove(complete_name)
            print(f"Congratulations for finishing {complete_name}!")
        except ValueError:
            print("That  item doesn't exist. Guess it is already done then?")
            continue

    elif to_do_action.lower() == "edit":
        if len(to_do_list) == 0:
            print("There are no items to finish.")
            continue
        try:
            number = input("Number of item to edit: ").strip()
            number = int(number) - 1
            to_do_list[number] = input("Enter replacement item: ")
        except IndexError:
            print("Error, that item doesn't exist.")
            continue
        except ValueError:
            print("Error, invalid input.")
            continue

    elif to_do_action.lower().startswith("add"):
        to_do_list.append(to_do_action[3:].strip())

    elif to_do_action.lower().startswith("edit"):
        if len(to_do_list) == 0:
            print("There are no items to finish.")
            continue
        try:
            edit_index = to_do_action[4:].strip()
            edit_index = int(edit_index) - 1
            to_do_list[edit_index] = input("Enter the new to do item: ")
        except ValueError:
            print("Error, invalid input. Please enter an index number.")
            continue
        except IndexError:
            print("Error, that item does not exist.")
            continue

    elif to_do_action.lower().startswith("delete"):
        delete_index = to_do_action[6:].strip()
        if len(to_do_list) == 0:
            print("There's nothing to delete.")
            continue
        try:
            delete_index = int(delete_index) - 1
            removed_item = to_do_list.pop(delete_index)
            print(f"Successfully deleted {removed_item}")
        except IndexError:
            print("Error, that item does not exist.")
            continue
        except ValueError:
            print("Error, please enter an index number.")
            continue

    elif to_do_action.lower().startswith("finish"):
        if len(to_do_list) == 0:
            print("There are no items to finish.")
            continue
        try:
            finish_item = to_do_action[6:].strip()
            to_do_list.remove(finish_item)
            print(f"Congratulations for finishing {finish_item}!")
        except ValueError:
            print("Error, that item does not exist.")
            continue

    elif to_do_action.lower() == "end":
        break

    else:
        print("Error, invalid input.")
        continue

    # Write all changes to file, if any.
    write_to_do_list("files/todo-data.txt", to_do_list)

    # Read the updated file and update the list.
    to_do_list = read_to_do_list("files/todo-data.txt")

print("Thank you for using the to do tracker application!")
