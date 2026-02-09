import random

# hint: look at main
def print_rules():
    rules = {
        "fjallbo": ["soderhamn", "tornviken"],
        "soderhamn": ["bjorksnas", "gronlid"],
        "bjorksnas": ["fjallbo", "tornviken"],
        "tornviken": ["gronlid", "soderhamn"],
        "gronlid": ["fjallbo", "bjorksnas"]
    }
    return rules, list(rules)


def call(choices, rules, rounds, user_wins, computer_wins):
    while True:
        play = input("Would you like to play a round? (y/n): ").lower()

        if play == "n":
            break
        elif play != "y":
            print("Please enter 'y' or 'n'.")
            continue

        rounds += 1
        user_move = user_turn(choices)
        user_wins, computer_wins = rule(user_move, choices, rules, user_wins, computer_wins)

    return rounds, user_wins, computer_wins


def user_turn(choices):
    user_move = ""
    while user_move not in choices:
        user_move = input("Enter your move (Tornviken, Bjorksnas, Soderhamn, Gronlid, Fjallbo): ").strip().lower()
        if user_move not in choices:
            print("Invalid move. Try again.")
    return user_move


def rule(user_move, choices, rules, user_wins, computer_wins):
    computer_move = random.choice(choices)

    print(f"You chose: {user_move}")
    print(f"Computer chose: {computer_move}")

    if user_move == computer_move:
        print("Result: Tie! Computer get a point")
        #return user_wins, computer_wins
        computer_wins += 1

    elif computer_move in rules[user_move]:
        print("Result: You win! You get a point")
        user_wins += 1
    else:
        print("Result: Computer wins! Computer gets a point")
        computer_wins += 1

    return user_wins, computer_wins


def guide():
    print()
    print("Ok then:")
    print("The only guide you need:")
    print("Fjallbo beats Soderhamn, Tornviken")
    print("Soderhamn beats Bjorksnas, Gronlid")
    print("Bjorksnas beats Fjallbo, Tornviken")
    print("Tornviken beats Gronlid, Soderhamn")
    print("Gronlid beats Fjallbo, Bjorksnas")
    print()


def main():
    rounds = 0
    user_wins = 0
    computer_wins = 0

    rules, choices = print_rules()

    print("Welcome to a game where you basically play.")
    answer = input("Need a guide? (y/n): ").lower()

    if answer == "y":
        guide()

    rounds, user_wins, computer_wins = call(choices, rules, rounds, user_wins, computer_wins)

    print()
    print(f"Rounds played: {rounds}")
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    print("Done")


main()

