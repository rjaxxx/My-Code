carsthatbeat = []
while True:
    try:
        car = int(input("What car just went past? "))
        if car <= 0:
            print("That is an invalid input")
        if car <= 20 and car > 0:
            break
        if car == 99:
            break
        else:
            carsthatbeat.append(car)
    except ValueError:
        print("That is an invalid input")
for item in carsthatbeat:
    print(item)
