# set variables and import func#
import random
import time
import os
money = 0
inventory = []
print('\n' * os.get_terminal_size().lines)

# randomised loop#

# number of cases#
number = int(input("Number of cases: "))
cost = number * 200
print("Cost: $" + str(cost))

# generator#
for i in range(number):
    # knives data#
    knives = [
        "Falchion Knife",
        "Shadow Daggers",
        "Paracord Knife",
        "Nomad Knife",
        "Flip Knife",
        "Ursus Knife",
        "Gut Knife",
        "Talon Knife",
        "Butterfly Knife",
        "Karambit",
        "Bayonet",
        "M9 Bayonet",
        "Skeleton Knife",
        "Survival Knife",
        "Bowie Knife",
        "Navaja Knife",
        "Classic Knife",
        "Stiletto Knife",
        "Huntsman Knife",
        "Kukri Knife",
    ]
    knife = random.choice(knives)

    # skins data#
    skins = [
        "Blue Gem",
        "Fade",
        "Vanilla",
        "Doppler",
        "Emerald Doppler",
        "Ruby Doppler",
        "Sapphire Doppler",
        "Slaughter",
        "Crimson Web",
        "Blue Steel",
        "Bright Water",
        "Rust Coat",
        "Lore",
        "Night",
    ]
    skin = random.choice(skins)

    # float data#
    floa = random.random()
    # boring float stuff try not to break this please#
    if float(floa) < 0.07:
        floa = "[Factory New]"
    elif float(floa) < 0.15:
        floa = "[Minimal Wear]"
    elif float(floa) < 0.38:
        floa = "[Field Tested]"
    elif float(floa) < 0.45:
        floa = "[Well Worn]"
    elif float(floa) < 1:
        floa = "[Battle Scarred]"

    # karambit blue gem#
    if knife == "Karambit" and skin == "Blue Gem" and floa == "[Factory New]":
        print("Karambit - [Blue Gem] - [Factory New]")
        money = money + 2000000
        print("OH MY GOD!!")
        print("Balance: $" + str(money))
        time.sleep(2)

    # value data#
    if "Butterfly Knife" in knife:
        money = money + 1500
    if "Karambit" in knife:
        money = money + 2000
    if "M9 Bayonet" in knife:
        money = money + 1000
    if "Bayonet" in knife:
        money = money + 500
    if "Gut Knife" in knife:
        money = money + 200
    if "Shadow Daggers" in knife:
        money = money + 150
    if "Falchion Knife" in knife:
        money = money + 50
    if "Parachord Knife" in knife:
        money = money + 50
    if "Nomad Knife" in knife:
        money = money + 50
    if "Flip Knife" in knife:
        money = money + 50
    if "Ursus Knife" in knife:
        money = money + 50
    if "Talon Knife" in knife:
        money = money + 50
    if "Skeleton Knife" in knife:
        money = money + 100
    if "Navaja Knife" in knife:
        money = money + 50
    if "Parachord Knife" in knife:
        money = money + 50
    if "Stiletto Knife" in knife:
        money = money + 50
    if "Survival Knife" in knife:
        money = money + 50
    if "Bowie Knife" in knife:
        money = money + 50
    if "Classic Knife" in knife:
        money = money + 200
    if "Kukri Knife" in knife:
        money = money + 1500

    # case opening#
    final = str(knife) + " - [" + str(skin) + "] - " + str(floa)
    print(final)
    inventory.append(final)
    money = money - 200
    print("Balance: $" + str(money))

# final print#
profit = money - cost
print("Profit: $" + str(profit))

# inventory#
final = input("Do you want to see your inventory? y/n: ")

# print inventory#
if final == "y":
    for i in inventory:
        print(i)

    # save inventory to file#
    ask = input("Do you want to save it as a file? y/n: ")
    if ask == "y":
        with open("inventory.txt", "w") as f:
            for i in inventory:
                print(i, file=f)
            print("Cost: $" + str(cost), file=f)
            print("Balance: $" + str(money), file=f)
            print("Profit: $" + str(profit), file=f)
    else:
        print("ok alg now reset the code")

else:
    print("ok alg now reset the code")
