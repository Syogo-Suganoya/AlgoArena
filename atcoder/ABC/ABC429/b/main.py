N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
A_set = set(A)

for a in A_set:
    if total - a == M:
        print("Yes")
        break
else:
    print("No")
