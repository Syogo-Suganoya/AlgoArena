N, M = map(int, input().split())
max_A = -float("inf")
min_B = float("inf")

for i in range(M):
    A, B = map(int, input().split())
    max_A = max(max_A, A)
    min_B = min(min_B, B)

if max_A > min_B:
    print(0)
else:
    print(min_B - max_A + 1)
