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
file_names = ["a.txt", "b.txt", "c.txt"]
for file_name in file_names:
    file = open(f"files/{file_name}")
    print(file.read().strip("\n"))



