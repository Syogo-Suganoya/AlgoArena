N = int(input())

Sl = []
max_len = -1
for _ in range(N):
    S = input()
    Sl.append(S)
    max_len = max(max_len, len(S))

for s in Sl:
    L = len(s)
    left = (max_len - L) // 2
    right = max_len - L - left
    print("." * left + s + "." * right)
