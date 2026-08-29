"""
Number Guessing Game Uses random module, loops, conditionals, and functions
"""
import random
def play_round(lower, upper, max_attempts):
    secret_number = random.randint(lower, upper)
    attempts = 0
    
    print(f"\nI'm thinking of a number between {lower} and {upper}.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    while attempts < max_attempts:
        guess = input("Enter your guess: ").strip()
        if not guess.isdigit():
            print("Please enter a valid number.\n")
            continue
        guess = int(guess)
        attempts += 1
        if guess < secret_number:
            print("Too low!\n")
        elif guess > secret_number:
            print("Too high!\n")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            return True
        
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts remaining: {remaining}\n")
            
    print(f"Out of attempts! The number was {secret_number}.")
    return False

def main():
    print("=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)
    
    lower = 1
    upper = 100
    max_attempts = 7
    
    wins = 0
    rounds_played = 0
    
    while True:
        won = play_round(lower, upper, max_attempts)
        rounds_played += 1
        if won:
            wins += 1
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            break
    print("\n" + "=" * 40)
    print(f"Rounds played: {rounds_played}")
    print(f"Rounds won: {wins}")
    print("Thanks for playing!")
    print("=" * 40)

    
if __name__ == "__main__":
    main()
