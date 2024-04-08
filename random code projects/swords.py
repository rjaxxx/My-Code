# set variables and import func#
import random
import os
money = 0
inventory = []
print('\n' * os.get_terminal_size().lines)

# randomised loop#

# number of cases#
number = int(input("Number of swords: "))
cost = number * 200
print("Cost: $" + str(cost))

# generator#
for i in range(number):
    # knives data#
    swords = [
        "Katana",
        "Dagger",
        "Knife",
        "Greatsword",
        "Broadsword",
        "Sword",
        "Rapier",
        "Skimitar",
        "Cutlass",
        "Longsword",
        "Backsword",
        "Claymore",
        "Falchion",
        "Sabre",
        "Hooked Sword",
        "Spiked Sword",
    ]
    sword = random.choice(swords)

    # skins data#
    skins = [
        "Galaxy",
        "Fade",
        "Vanilla",
        "Steel",
        "Red Steel",
        "Blue Steel",
        "Green Steel",
        "Emerald",
        "Silver",
        "Gold",
        "Bronze",
        "Ruby",
        "Sapphire",
        "Ancient",
        "Bloodied",
        "Pristine",
    ]
    skin = random.choice(skins)

    # element data#
    element = random.random()
    # boring float stuff try not to break this please#
    if float(element) < 0.07:
        element = "[Shadow Element]"
    elif float(element) < 0.15:
        element = "[Fire Element]"
    elif float(element) < 0.38:
        element = "[Frost Element]"
    elif float(element) < 0.45:
        element = "[Lightning Element]"
    elif float(element) < 1:
        element = "[No Element]"

    # value data#
    if "Katana" in sword:
        money = money + 1500
    if "Greatsword" in sword:
        money = money + 2000
    if "Broadsword" in sword:
        money = money + 1000
    if "Sword" in sword:
        money = money + 500
    if "Rapier" in sword:
        money = money + 200
    if "Dagger" in sword:
        money = money + 150
    if "Falchion" in sword:
        money = money + 50
    if "Skimitar" in sword:
        money = money + 50
    if "Cutlass" in sword:
        money = money + 50
    if "Longsword" in sword:
        money = money + 50
    if "Backsword" in sword:
        money = money + 50
    if "Talon Knife" in sword:
        money = money + 50
    if "Claymore" in sword:
        money = money + 100
    if "Sabre" in sword:
        money = money + 50
    if "Hooked Sword" in sword:
        money = money + 50
    if "Spiked Sword" in sword:
        money = money + 50

    # case opening#
    final = str(sword) + " - [" + str(skin) + "] - " + str(element)
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
