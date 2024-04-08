'''NCEA Practice Question - Rory Collins'''

# Variable amounts#
balance = 200
money = [200]

# Get amount spent#
while True:
    try:
        amount = int(input("Enter the amount spent: "))
        if amount == 0:
            break
        balance -= amount
        money.append(balance)
        if balance <= 0:
            break
    except ValueError:
        print("That is not a valid transaction.")

# Print bank balances#
print("My bank balances have been:")
for item in money:
    print(item)
