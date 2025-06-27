import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("\n Welcome to the Dice Roller! ")

    for _ in range(3):  # Simulate 3 dice rolls
        print("\nRolling the dice...")
        result = roll_dice()
        print(f"You rolled a {result}!")

    print("\nThanks for playing! Goodbye ")

if __name__ == "__main__":
    main()
