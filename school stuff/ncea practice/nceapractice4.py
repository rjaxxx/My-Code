'''Program to tell you whether a temperature is too hot or too cold (8/3/24)
Rory Collins'''

# create list for temperature#
temperatures = []
LOWERLIMIT = 34
UPPERLIMIT = 42
ENDCODE = -1

# indefinite loop#
while True:
    try:

        # taking input#
        number = int(input("Enter the temperature: "))

        # checking if number is negative and ending loop if true#
        if number == ENDCODE:
            break
        else:
            # check temperature and then append to list#
            if number < LOWERLIMIT:
                temperatures.append('too cold')
            elif number > UPPERLIMIT:
                temperatures.append('too hot')
            elif number >= LOWERLIMIT and number <= UPPERLIMIT:
                temperatures.append('just right')

    # invalid cases#
    except ValueError:
        print("Invalid temperature.")

# print temperature list line by line#
for i in temperatures:
    print(i)
