S = input()
T = input()

if T[-1] == "X":
    T = T[:-1]

b = 0

for c in T.lower():
    pos = S.find(c, b)
    if pos == -1:
        print("No")
        break
    b = pos + 1
else:
    print("Yes")
