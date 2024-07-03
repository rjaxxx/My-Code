# create list for robot language#
robots = []
ZERO = 0
UPPERLIMIT = 512

# indefinite loop#
while True:
    try:
        # taking input#
        number = int(input("Enter your input: "))
        # checking number values and adding to list#
        if number < ZERO:
            break
        if number <= UPPERLIMIT:
            robots.append('Boop')
        if number > UPPERLIMIT:
            robots.append("Beep")
    # invalid cases#
    except ValueError:
        print("Not robot compliant!")

# final print of the robot list on each line#
for i in robots:
    print(i)
