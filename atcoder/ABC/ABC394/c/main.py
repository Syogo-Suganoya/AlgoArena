S = list(input())

for i in range(len(S) - 1, 0, -1):
    if S[i - 1] + S[i] == "WA":
        S[i - 1] = "A"
        S[i] = "C"
print("".join(S))
