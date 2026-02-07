import random


rules = {
    "fjallbo": ["soderhamn", "tornviken"],
    "soderhamn": ["bjorksnas", "gronlid"],
    "bjorksnas": ["fjallbo", "tornviken"],
    "tornviken": ["gronlid", "soderhamn"],
    "gronlid": ["fjallbo", "bjorksnas"]
}
choices = list(rules)# call the 2 list in rules (its a dictionary function) 


print("Game rules: ")
print("Fjallbo beats Soderhamn, Tornviken")
print("Soderhamn beats Bjorksnas, Gronlid")
print("Bjorksnas beats Fjallbo, Tornviken")
print("Tornviken beats Gronlid, Soderhamn")
print("Gronlid beats Fjallbo, Bjorksnas")
print()

rounds = 0
user_wins = 0
computer_wins = 0

while True:
    play = input("Would you like to play a round? (y/n): ").lower()
    if play == "n":
        break
    elif play != "y":
        print("Please enter 'y' or 'n'.")
        continue

    rounds += 1

    user_move = ""
    while user_move not in choices:
        user_move = input("Enter your move (Tornviken, Bjorksnas, Soderhamn, Gronlid, Fjallbo): ").strip().lower()
        if user_move not in choices:
            print("Invalid move. Try again.")
    computer_move = random.choice(choices)
    print(f"You chose: {user_move}")
    print(f"Computer chose: {computer_move}")

    if user_move == computer_move:
        print("Result: Tie!")
        computer_wins += 1
    elif computer_move in rules[user_move]: 
        print("Result: You win!")
        user_wins += 1
    else:
        print("Result: Computer wins!")
        computer_wins += 1
print()
print(f"Rounds played: {rounds}")
print(f"User wins: {user_wins}")
print(f"Computer wins: {computer_wins}")
print("Done")