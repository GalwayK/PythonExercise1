number_heads = 0.0
number_tails = 0.0
total_flips = 0

try:
    with open("files/coins.txt", "r") as file:
        for line in file:
            line = line.strip("\n")
            match line:
                case "heads":
                    total_flips = total_flips + 1
                    number_heads = number_heads + 1
                case "tails":
                    total_flips = total_flips + 1
                    number_tails = number_tails + 1
except IOError:
    pass

print("Welcome to the coin counter program!\nEnter heads or tails to increment the counter, or end to stop "
      "the program.")
while True:
    user_input = input(f"Total flips: {total_flips}\nPlease enter heads, tails, or end: ").strip().lower()
    match user_input:
        case "heads":
            print("Entering heads.")
            total_flips = total_flips + 1
            number_heads = number_heads + 1
        case "tails":
            print("Entering tails.")
            total_flips = total_flips + 1
            number_tails = number_tails + 1
        case 'end':
            break
        case default:
            print("Well, that didn't make any sense.")
            continue
    print(f"Total heads: {int(number_heads)} The percent of heads: {(number_heads / total_flips) * 100}")
    print(f"Total tais: {int(number_tails)} The percent of tails: {(number_tails / total_flips) * 100}")
    with open("files/coins.txt", "a+") as file:
        print("Writing to file.")
        file.write(f"{user_input}\n")
print("See you later!")
