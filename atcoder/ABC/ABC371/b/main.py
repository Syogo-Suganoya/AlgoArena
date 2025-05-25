N, M = map(int, input().split())
l = [False] * N
for i in range(M):
    A, B = input().split()
    if B == "F":
        print("No")
        continue
    A = int(A) - 1
    if l[A]:
        print("No")
        continue
    l[A] = True
    print("Yes")
