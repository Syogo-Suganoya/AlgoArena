N, L, R = map(int, input().split())
S = input()
for i in range(L - 1, R):
    if S[i] == "x":
        print("No")
        break
else:
    print("Yes")
