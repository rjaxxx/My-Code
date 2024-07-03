from PIL import Image
import os
import random
import time

dragonbreath = "H:\\CODE\\random code projects\\kadengame\\dragonbreath.png"
cyber = "H:\\CODE\\random code projects\\kadengame\\cyber.png"
bluesword = "H:\\CODE\\random code projects\\kadengame\\bluesword.png"

print("\n" * os.get_terminal_size().lines)

# WELCOME#
print("WELCOME TO SWORD SIMULATOR (BETA)")

# number of cases#
amount = int(input("Number of swords: "))

for i in range(amount):
    number = random.randint(0, 1000)

    if number > 900 and number < 950:
        # Open the image file
        try:
            image = Image.open(dragon)
            # Show the image
            image.show()
            print("\n" * os.get_terminal_size().lines)
            print("WOW THATS RARE!! (1/20)")
            time.sleep(1)
            Image.close()


        except:
            print("image died my bad lol")

    if number > 990:
        # Open the image file
        try:
            image = Image.open(cyber)
            # Show the image
            image.show()
            print("\n" * os.get_terminal_size().lines)
            print("WOW THATS RARE!! (1/100)")
            time.sleep(1)
            Image.close()

        except:
            print("image died my bad")
    if number < 900:
        try:
            image = Image.open(bluesword)
            # Show the image
            image.show()
            print("\n" * os.get_terminal_size().lines)
            print("Unlucky...")
            time.sleep(1)
            Image.close()

        except:
            print("image died my bad")
