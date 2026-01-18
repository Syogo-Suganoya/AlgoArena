from sortedcontainers import SortedSet

N, M = map(int, input().split())
S = input()
T = input()
Q = int(input())

setS = SortedSet(S)
setT = SortedSet(T)

for _ in range(Q):
    W = input()
    setW = SortedSet(W)

    res1 = setS >= setW
    res2 = setT >= setW

    if res1 and res2:
        print("Unknown")
    elif res1:
        print("Takahashi")
    elif res2:
        print("Aoki")
    else:
        print("Unknown")
