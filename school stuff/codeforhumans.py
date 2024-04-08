'''Simple and readable program to see if a user is able to vote in NZ or not
by Rory Collins (Helped by SRCoder aka Mr Rodkiss)'''
is_resident = False
# ask the users name
name = input("What is your name?\n")
while True:
    try:
        # ask the users age
        age = int(input("How old are you?\n"))
        break
    except:
        print("That is not a number\n")
# end of while loop
age = int(age)
# asks if they are a resident
while True:
    resident = input("Are you a resident? Y/N\n")
    if resident.lower() == 'y':
        is_resident = True
        break
    elif resident.lower() == 'n':
        is_resident = False
        break
    else:
        print('Please type in either Y or N')
# evaluate if person can vote
if age > 17 and is_resident:
    print("You can vote\n")
else:
    print("You cannot vote\n")
