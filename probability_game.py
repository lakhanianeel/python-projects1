import random

def play_guessing_game():
    name = input("Enter your name: ")
    prize_money = 1000
    number_to_guess = random.randint(1, 1000)
    attempts = 10
    print("\nWelcome to the Guessing Game!\n")
    print("You have a chance to win $10 or play the guessing game.\n")
    choice = input("Enter 'W' to win $10 or 'G' to play the guessing game: ")

    if choice.upper() == 'W':
        print(f"\nCongratulations, {name}! You won $10!\n")
    elif choice.upper() == 'G':
        print("\nLet's play the guessing game!")
        print("You have 10 chances to guess a number between 1 and 1000.\n")

        for _ in range(attempts):
            print(f"Prize Money: ${prize_money}")
            print(f"Attempts left: {attempts}\n")
            guess = int(input("Enter your guess: "))

            if guess == number_to_guess:
                print(f"\nCongratulations, {name}! You guessed the correct number!")
                print(f"Ending Prize Money: ${prize_money}\n")
                break
            elif guess > number_to_guess:
                print("\nToo high!")
            else:
                print("\nToo low!")

            prize_money = round(prize_money / 2)
            attempts -= 1
        else:
            print(f"Sorry, {name}. You should have taken the $10.")
            print(f"The correct number was: {number_to_guess}")
            print('You owe $5\n')
    else:
        print("Invalid choice.")

play_guessing_game()
