'''A simple program that tests to see if user can guess the number
their friend has thought of. - NCEA Question 2 - Rory Collins'''

# create variables and lists#
CORRECTNUMBER = 4
UPPERLIMIT = 10
LOWERLIMIT = 1
guesses = []

# create indefinite loop#
while True:

    # use try to account for invalid inputs#
    try:

        # take input and save it as a variable named 'guess'#
        guess = int(input("Guess a number from 1 to 10: "))

        # check if guess is correct or not#
        if guess == CORRECTNUMBER:
            # add guess to list#
            guesses.append(guess)
            # if guess is correct print correct and break loop#
            print("Correct.")
            break

        # check if guess is above lowerlimit (in this case 1) and under
        # upperlimit (in this case 10)#
        if guess >= LOWERLIMIT and guess <= UPPERLIMIT:
            # if true add it to list and print incorrect##
            guesses.append(guess)
            print("Incorrect.")

        else:
            # if the guess is not between lowerlimit and upperlimit tell user
            # it isn't and ignore#
            print(f"That is not between {LOWERLIMIT} and {UPPERLIMIT}.")

    # use except to print invalid guess if guess is invalid#
    except ValueError:
        print("That is an invalid guess.")

# print guesses as a list, line by line#
print("Here are your guesses:")
for item in guesses:
    print(item)
