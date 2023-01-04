import json
import glob
file = glob.glob("*/questions.json")
print(file)
with open(file[0], "r") as file:
    content = file.read()
data = json.loads(content)


print("\nWelcome to the game!")
correct_count = []
for index, question in enumerate(data):
    print(f'Question {index + 1}. {question["question_text"]}')
    for question_text in question["answer_text"]:
        print(f"{question_text}")
    while True:
        answer = input("Which answer is correct: ")
        try:
            if float(answer) == question["answer_num"]:
                correct_count.append(True)
                print(f'Your answer: {question["answer_text"][int(answer) - 1]}')
                print(f'Correct Answer: {question["answer_text"][question["answer_num"] - 1]}')
                break
            elif float(answer) > len(question["answer_text"]) or float(answer) < 1:
                print("Please enter a valid number.")
                continue
            else:
                correct_count.append(False)
                print(f'Your answer: {question["answer_text"][int(answer) - 1]}')
                print(f'Correct Answer: {question["answer_text"][question["answer_num"] - 1]}')
                break
        except ValueError:
            print("Please enter the number of the answer.")
            continue

if all(correct_count):
    print("Fantastic, all correct!")
else:
    print(f"You had {correct_count.count(True)} correct out of {len(data)}. Better luck next time.")


