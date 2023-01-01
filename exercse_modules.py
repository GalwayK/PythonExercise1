# import glob
#
# myfiles = glob.glob("*/*.txt")
#
# for index, filename in enumerate(myfiles):
#     with open(filename, "r") as file:
#         print(file.readline())
#
# print(myfiles)
#
# import csv
# with open("files/weather.csv") as file:
#     data = list(csv.reader(file))
# #     print(data)
# import csv
# city = input("Enter your city: ")
# with open("files/weather.csv") as file:
#     data = list(csv.reader(file))
#
# city_found = False
# for column in data[1:]:
#     if column[0] == city:
#         print(f"Temperature: {column[1]}")
#         city_found = True
#
# if not city_found:
#     print("City not found.")

# import shutil
#
# shutil.make_archive("output", "zip", "files")


import webbrowser

search_term = input("Please enter a search term: ")
webbrowser.open(f"https://google.com/search?q={search_term}")
