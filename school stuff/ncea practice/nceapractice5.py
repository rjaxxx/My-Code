# create list of scores and variable#
scores = []
smart = 0
GOODSCORE = 80
ONE = 1
END = 'done'

# create indefinite loop#
while True:
    try:

        # get score input#
        score = input("Enter a score, or type 'done' to exit: ")
        if score == END:
            break
        score = int(score)

        # add score to list if it is above what qualifies as a good score#
        if score >= GOODSCORE:
            scores.append(score)
            smart = smart + ONE

    # account for invalid input#
    except ValueError:
        print("Invalid score!")

# final print of smart students#
if smart == ONE:
    print(f'This class has {smart} smart student!')
else:
    print(f'This class has {smart} smart students!')
