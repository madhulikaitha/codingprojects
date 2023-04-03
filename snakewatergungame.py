import random

while True:
    options = ["snake","water","gun"]

    computer = random.choice(options)

    def selected_option():
        player = input("Snake, water, gun: ").lower()
        if player in options: 
            print("computer chooses:",computer)
            print("player chose:",player)
        else:
            print("Please only select snake, water or gun")

        if player == computer:
            print("It's a tie")
        elif player == "snake":
            if computer == "water":
                print("You win")
            if computer == "gun":
                print("You lose")
        elif player == "water":
            if computer == "snake":
                print("You lose")
            if computer == "gun":
                print("You win")
        elif player == "gun":
            if computer == "water":
                print("You lose")
            if computer == "snake":
                print("You win")

    selected_option = selected_option()
    play_again = input("Would you like to play again (yes/no): ").lower()
    if play_again != "yes":
        break

print("BYEEEEEE!")