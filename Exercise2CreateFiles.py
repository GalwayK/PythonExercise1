# contents = ["Add carrots are to be sliced.", "The carrots are sliced."]
# string = "The carrots were " \
#     "cut."
# contents.append(string)
#
# file_names = ["doc.txt", "report.txt", "presentation.txt"]
#
# for content, file_name in zip(contents, file_names):
#     file = open(f"../Project1-ToDoListConsole/files/{file_name}", "w")
#     file.write(f"{content}\n")

# file = open("files/essay.txt")
# file_lines = []
# length = 0
# for line in file:
#     length = length + len(line)
#     line = line.strip("\n")
#     file_lines.append(line.title())
# print(f"Lines: {file_lines}")
# print(f"Length: {length}")

# members_file = open("files/members.txt", "r")
# members_list = []
# for member in members_file:
#     member = member.strip("\n")
#     members_list.append(member)
# members_file.close()
# print(members_list)
# while True:
#     user_action = input("Would you like to add a new user: ").lower()
#     match user_action:
#         case "yes":
#             new_user = input("Enter user's name: ")
#             members_list.append(new_user)
#         case "no":
#             break
#         case default:
#             print("Sorry, didn't understand that.")
#     members_file = open("files/members.txt", "w")
#     for member in members_list:
#         members_file.write(f"{member}\n")
#     members_file.close()
#
# print("Thank you for using this program!")
#
# file_names = ["fileOne.txt", "fileTwo.txt", "fileThree.txt"]
#
# for file_name in file_names:
#     file = open(f"files/{file_name}", "w")
#     file.write("Hello!\n")
# file_names = ["a.txt", "b.txt", "c.txt"]
# for file_name in file_names:
#     file = open(f"files/{file_name}")
#     print(file.read().strip("\n"))

# file_names = ["1.report", "2.doc", "3.txt"]
# new_names = [f"{name.replace('.', '-')}.txt" for name in file_names]
# for index, name in enumerate(new_names):
#     print(f"{name}")

# names = ["kyle galway", "vicente angeles", "gavin shaw"]
#
# names_capital = [name.title() for name in names]
#
# print(names_capital)

# user_names = ["EasternEagle", "AigledeLest", "AnxiousAvian"]
#
# names_length = [len(name) for name in user_names]
#
# print(names_length)


# numbers = [10, 11, 12]
#
# numbers_float = [float(number) for number in numbers]
#
# print(numbers_float)
#
# print(sum(numbers))

# temperatures = [10, 12, 11]
#
# file = open("files/temps.txt", "w")
# [file.write(f"{temp}\n") for temp in temperatures]

numbers = [10.0, 11.1, 12.2]
numbers = [int(number) for number in numbers]
print(numbers)
