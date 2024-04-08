stories = int(input())
struts =  2
platforms = 1
for i in range(stories):
    struts += 2
    platforms += 1
cards = (struts + platforms)
print(cards)