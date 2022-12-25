password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result["is_long"] = True
else:
    result["is_long"] = False

result["has_digit"] = False
for char in password:
    if char.isdigit():
        result["has_digit"] = True


result["has_upper"] = False
for char in password:
    if char.isupper():
        result["has_upper"] = True

result["has_lower"] = False
for char in password:
    if char.islower():
        result["has_lower"] = True

print(result)

if all(result.values()):
    print("This is a strong password.")
else:
    print("This is a weak password.")
