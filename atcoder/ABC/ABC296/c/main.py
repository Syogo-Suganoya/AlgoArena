N, X = map(int, input().split())
A = list(map(int, input().split()))
A_set = set(A)

for a in A:
    if a + X in A_set:
        print("Yes")
        break
else:
    print("No")
