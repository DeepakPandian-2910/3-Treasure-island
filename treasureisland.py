print("Welcome to Treasure island.\nYour mission is to find the treasure.")
first = input("choose 'left' or 'right': ").lower()
if first == "left":
    second = input("choose to 'swim' or 'wait' for the boat: ").lower()
    if second == 'wait':
        print("You found three doors; red, yellow, blue colour doors.")
        third = input("Choose one door: ").lower()
        if third == "yellow":
            print("You found the treasure!!!")
        elif third == "red":
            print("You fell into a room full of beasts. Game over.")
        else:
            print("You fell into fire. Game over.")
    else:
        print("Sharks ate you. Game over.")
else:
    print("You fell in a hole. Game over.")
