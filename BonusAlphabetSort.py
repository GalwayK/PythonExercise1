athlete_list = ["Chris", "Ben", "Aaron"]
athlete_list.sort()

for index, athlete in enumerate(athlete_list):
    match index:
        case 0:
            row = f"{index + 1}st place is {athlete.capitalize()}"
        case 1:
            row = f"{index + 1}nd place is {athlete.capitalize()}"
        case 2:
            row = f"{index + 1}rd place is {athlete.capitalize()}"
        case default:
            row = "How did you do that?"
    print(row)
