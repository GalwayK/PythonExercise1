# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     grades_list = {}
#     grades_list["max"] = max(grades)
#     grades_list["min"] = min(grades)
#     return grades_list
#
#
# grades_list = get_max()
# for grade in grades_list.values():
#     print(grade)

# def get_maximum():
#     celsius_local = [14, 15.1, 12.3]
#     maximum = max(celsius_local)
#     print(maximum)
#     return maximum
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
# print(fahrenheit)

def get_temperature_average():
    with open("files/data.txt", "r") as file:
        data = file.readlines()
    try:
        data = [float(temp) for temp in data[1:]]
    except ValueError:
        print("Error, not a number.")
    print(data)
    average_temp = sum(data) / len(data)
    return average_temp


temperature_average = get_temperature_average()
print(temperature_average)

