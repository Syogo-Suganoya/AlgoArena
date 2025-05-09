N = int(input())
S = input()
T = input()

for i in range(N):
    a, b = S[i], T[i]
    if a == b:
        continue
    if (a == "1" and b == "l") or (b == "1" and a == "l"):
        continue
    if (a == "0" and b == "o") or (b == "0" and a == "o"):
        continue
    print("No")
    break
else:
    print("Yes")
