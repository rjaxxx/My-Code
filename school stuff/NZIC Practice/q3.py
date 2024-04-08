G = 0
C = 0
E = 0
P = 0
L = 0
S = 0
while True:
    teas = input()
    if teas == 'D':
        break
    else:
        teas = teas.split()
        if teas[0] == 'G':
            G += int(teas[1])
        if teas[0] == 'C':
            C += int(teas[1])
        if teas[0] == 'E':
            E += int(teas[1])
        if teas[0] == 'P':
            P += int(teas[1])
        if teas[0] == 'L':
            L += int(teas[1])
        if teas[0] == 'S':
            S += int(teas[1])
print(G, C, E, P, L, S)