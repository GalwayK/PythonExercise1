
with open("files/todo-data.txt", "r") as to_do_file:
    list_to_do = to_do_file.readlines()
to_do_list = [line.strip().strip("\n") for line in list_to_do]

print("Welcome, your current list is: ")
for index, to_do in enumerate(to_do_list):
    print(f"{index + 1}. {to_do}")
print("Welcome to the to do application!")

while True:
    to_do_action = input("Would you like to leave the application or add, edit, show, finish, or delete an item: ")\
        .strip()
    to_do_action = to_do_action.strip().strip("\n")

    if to_do_action.lower() == 'add':
        to_do_item = input("Type the name of the item: ").strip()
        to_do_list.append(to_do_item)
    elif to_do_action.lower() == "show" or to_do_action.lower() == "display":
        print("Displaying items.")
        to_do_list = [line.strip("\n") for line in to_do_list]
        for index, to_do in enumerate(to_do_list):
            print(f"{index + 1}. {to_do}")
    elif to_do_action.lower() == "delete" or to_do_action.lower() == "remove":
        if len(to_do_list) == 0:
            print("There are no items to delete.")
            continue
        delete_index = input("What item would you like to delete: ").strip()
        if delete_index.isdigit():
            delete_index = int(delete_index) - 1
        else:
            print("Error, not an index.")
            continue
        if len(to_do_list) > delete_index > -1:
            removed_item = to_do_list.pop(delete_index)
            print(f"Successfully deleted {removed_item}")
        else:
            print("Item does not exist.")
    elif to_do_action.lower() == "finish" or to_do_action.lower() == "complete":
        if len(to_do_list) == 0:
            print("There are no items to finish.")
            continue
        complete_name = input("Which item have you completed: ").strip()
        if to_do_list.__contains__(complete_name):
            to_do_list.remove(complete_name)
            print(f"Congratulations for finishing {complete_name}!")
        else:
            print("That item doesn't exist. Guess it's already done then?")
    elif to_do_action.lower() == "edit":
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
    elif "add" in to_do_action[0:3]:
        to_do_list.append(to_do_action[3:].strip())
    elif "edit" in to_do_action[0:4]:
        edit_index = to_do_action[4:].strip()
        if edit_index.isdigit():
            edit_index = int(edit_index) - 1
        else:
            print("Error, not an index.")
            continue
        if len(to_do_list) > edit_index > -1:
            to_do_list[edit_index] = input("Enter the new to do item: ")
        else:
            print("Error, that item is not being tracked.")
            continue
    elif "delete" in to_do_action[0:6]:
        delete_index = to_do_action[6:].strip()
        if delete_index.isdigit():
            delete_index = int(delete_index) - 1
        else:
            print("Error, not an index.")
            continue
        if len(to_do_list) > delete_index > -1:
            removed_item = to_do_list.pop(delete_index)
            print(f"Successfully deleted {removed_item}")
        else:
            print("Error, that item is not being tracked.")
    elif "finish" in to_do_action.lower()[0:6]:
        finish_item = to_do_action[6:].strip()
        if to_do_list.__contains__(finish_item):
            to_do_list.remove(finish_item)
            print(f"Congratulations for finishing {finish_item}!")
        else:
            print("That item doesn't exist. Guess it is done already then?")


    elif "end" in to_do_action:
        break
    else:
        print("Error, invalid input.")
        continue

    # Write all changes to file, if any.
    with open("files/todo-data.txt", "w") as to_do_file:
        for to_do in to_do_list:
            to_do_file.write(f"{to_do}\n")

    # Read the updated file and update the list.
    with open("files/todo-data.txt", "r") as to_do_file:
        list_to_do = to_do_file.readlines()
    to_do_list = [line.strip().strip("\n") for line in list_to_do]

print("Thank you for using the to do tracker application!")
