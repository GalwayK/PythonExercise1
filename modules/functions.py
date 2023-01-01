def write_to_do_list(to_do_list_local, filepath="files/todo-data.txt"):
    """
    Reads a list of todo items and writes them to the given file, overwriting the file's contents in the process.
    If file is unspecified, attempts to write to a default file location.
    """
    print("Writing data...")
    with open(filepath, "w") as file:
        [file.write(f"{line}\n") for line in to_do_list_local]
    print("Writing done!")
    return None


def read_to_do_list(filepath="files/todo-data.txt"):
    """
    Reads data from a file and returns each line as a String without trailing whitespaces or new lines.
    Saves each line in a list and returns the list.
    """
    print("Reading data...")
    with open(filepath, "r") as file:
        to_do_list_local = file.readlines()
    print("Reading done!")
    return [line.strip().strip("\n") for line in to_do_list_local]


def show_to_do_list(to_do_list_local):
    """
    Receive a list and displays the list's content to the console in a numbered list.
    """
    print("Displaying list: ")

    for index, to_do in enumerate(to_do_list_local):
        print(f"{index + 1}. {to_do}")
    return None


print(__name__)
if __name__ == "__main__":
    print(__name__)

