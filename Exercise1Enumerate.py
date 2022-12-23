# file_names = ["document", "report", "presentation"]
# for index, file_name in enumerate(file_names):
#     print(f"{index + 1}. {file_name.capitalize()}")

ips = ['100.122.133.105', '100.122.133.111']
index = int(input("Enter an index: ")) - 1
if -1 < index < len(ips):
    print(f"IP Address: {ips[index]}")
else:
    print("An error has occured.")


