# try:
#     width = input("Enter the width of the rectangle: ")
#     width = float(width)
#     length = input("Enter the length of the rectangle: ")
#     length = float(length)
#     if length == width:
#         exit("Error, not a rectangle.")
#     area = width * length
# except ValueError:
#     print("Error, enter a numeric.")
try:
    total_value = input("Enter the total value: ")
    total_value = float(total_value)
    part_value = input("Enter the partial value: ")
    part_value = float(part_value)
    percentage_value = part_value / total_value
    print(f"The percentage is {percentage_value * 100}%")
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("Error, total value cannot be 0.")
