date = input("Enter the current date: ")

while True:
    mood = input("Enter your current mood on 1-10: ")
    if mood.isdigit():
        mood = int(mood)
        break
    else:
        print("Error, not a number.")
        continue

entry = input("Write your journal entry:\n")

with open(f"files/{date}", "w") as file:
    file.write(f"Your mood: {mood}\n")
    file.write(f"Entry:\n{entry}")
print("Thank you for writing today. It is important to let your thoughts be known.")
