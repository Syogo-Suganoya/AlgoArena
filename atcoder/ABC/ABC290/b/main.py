N, M = map(int, input().split())
S = input()

count = 0
e = 0
res = ""
for i, c in enumerate(S):
    if c == "o":
        count += 1
    if count >= M:
        e = i
        break

print(S[: e + 1] + "x" * (N - e - 1))
