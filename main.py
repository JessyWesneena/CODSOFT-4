import random

choices = ["rock", "paper", "scissors"]

# Function to decide winner
def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"


def main():
    user_score = 0
    computer_score = 0

    print("---- ROCK PAPER SCISSORS GAME ----")

    while True:
        print("\nChoose: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in choices:
            print("Invalid choice! Try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "win":
            print("🎉 You win!")
            user_score += 1
        elif result == "lose":
            print("😢 You lose!")
            computer_score += 1
        else:
            print("🤝 It's a tie!")

        print(f"\nScore → You: {user_score} | Computer: {computer_score}")

        # Ask to play again
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break


# Run program
if __name__ == "__main__":
    main()