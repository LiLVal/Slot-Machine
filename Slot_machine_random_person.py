from random import choice

money = 0.2
items = ["Skull", "Cherry",]
#"Bell", "Lemon", "Star", "Orange"
roll_three = []

def check_winnings():
    check_all = roll_three.count(roll_three[0]) == len(roll_three)
    check_skull = roll_three.count("Skull") == len(roll_three)
    if (check_skull):
        print("bruh")

def roll():
    if money < 0.2:
        print("Not enough money")
    else:
        roll_three.clear()
        for i in range(3):
            roll_three.append(choice(items))
        print(roll_three)
        check_winnings()

def start_game():
    option = 0
    while option != 2:
        try:
            option = int(input("Press 1 to roll | Press 2 to end: "))
            if option == 1:
                roll()
            elif option == 2:
                print("Winnings total is: {}".format(money))
        except ValueError:
            print("Please enter either '1' or '2'")

start_game()

