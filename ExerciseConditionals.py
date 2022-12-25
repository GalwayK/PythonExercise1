# password = input("Please enter a password: ")
#
# if len(password) >= 8:
#     print("Great password!")
# elif len(password) == 7:
#     print("Password is okay.")
# else:
#     print("Weak password.")

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")