file_names = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")

for index, file_name in enumerate(file_names):
    file_name = file_name.replace(".", "-", 1)
    print(file_name)
print(file_names)
