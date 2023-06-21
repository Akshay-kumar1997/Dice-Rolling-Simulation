import random

def roll_dice():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

def main():
    play_again = True

    while play_again:
        input("Press Enter to roll the dice...")
        dice_value = roll_dice()
        print("The dice rolled:", dice_value)

        play_again_input = input("Do you want to roll again? (yes/no): ")
        play_again = play_again_input.lower() == "yes"

    print("Thank you for playing!")

if __name__ == "__main__":
    main()

