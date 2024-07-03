"""Simple money clicker game for Kaden (8/3/24) - Rory"""

import time
import random
import os

# create var#
money = 0
mps = 1
cost = 2
totalmoney = 0
totalspent = 0
print("\n" * os.get_terminal_size().lines)

# make loop#
name = input("What is your name? ")

while True:
    try:
        timer = int(input("How many seconds do you want to farm money for? "))
        if timer == -500:
            money = 50000000

    except ValueError:
        print("Not a valid number.")
        timer = 0

    # add money#
    for i in range(timer):
        money += mps
        totalmoney += mps
        print(f"Money: ${money}")
        time.sleep(1)

    # shop query#
    shop = input("Enter shop? y/n: ")

    # shop entry
    if shop == "y":
        print(f"Money: ${money}")

        # upgrades#
        upgrade = input(f"Upgrade money per second? [${cost}] y/n: ")
        if money >= cost:
            if upgrade == "y":
                money -= cost
                cost += 10
                totalspent += cost
                mps += 1
        else:
            print("You don't have enough money yet...")

    # casion query#
    casino = input("Enter casino? y/n: ")

    # shop entry
    if casino == "y":
        print(f"Money: ${money}")
        gamble = input("Want to gamble your money? y/n: ")
        if gamble == "y":
            howmuch = int(input("How much money do you want to gamble? "))
            if howmuch < money:
                n = random.randint(0, 1000)
                if n > 500:
                    howmuch = howmuch * 2
                    print(f"You won ${howmuch}!")
                    money = money + howmuch
                    print(f"Money: ${money}")

                else:
                    money = money - howmuch
                    print(f"You lost ${howmuch}")
                    print(f"Money: ${money}")
            else:
                print("You don't have enough money...")
        else:
            print("Okay.")

    # checkpoints (not working)#

    # pc#
    if money > 1000:
        item2 = input("Want to buy a new PC? y/n: ")
        if item2 == "y":
            pc = input("What type of PC? ")
        print(f"Congratulations on your brand new {pc}, {name}!")

    # car#
    elif money > 5000:
        item1 = input("Want to buy a new car? y/n: ")
        if item1 == "y":
            car = input("What type of car? ")
        print(f"Congratulations on your brand new {car}, {name}!")

    # apartment#
    elif money > 10000:
        item2 = input("Want to buy a new apartment? y/n: ")
        if item2 == "y":
            location = input("Where will your apartment be? ")
        print(
            f"Congratulations on your brand new apartment "
            f"in {location}, {name}!")

    # house#
    elif money > 50000:
        item2 = input("Want to buy a new house? y/n: ")
        if item2 == "y":
            location = input("Where will your house be? ")
        print(
            f"Congratulations on your brand new house "
            f"in {location}, {name}!")

    # mansion#
    elif money > 100000:
        item2 = input("Want to buy a new mansion? y/n: ")
        if item2 == "y":
            location = input("Where will your mansion be? ")
        print(
            f"Congratulations on your brand new mansion "
            f"in {location}, {name}!")
