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


# import webbrowser
#
# search_term = input("Please enter a search term: ")
# webbrowser.open(f"https://google.com/search?q={search_term}")

import random

try:
    num_min = input("Enter the minimum value: ")
    num_min = int(num_min)
    num_max = input("Enter the maximum value: ")
    num_max = int(num_max)
    if num_min > num_max:
        number = random.randint(num_max, num_min)
    else:
        number = random.randint(num_min, num_max)
    print(f"The random number is {number}.")
except ValueError:
    print("Error, not a number.")
