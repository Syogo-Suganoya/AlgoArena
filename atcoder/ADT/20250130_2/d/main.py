N, A = map(int, input().split())
T = list(map(int, input().split()))

pre = 0
for i in T:
    pre = max(pre, i) + A
    print(pre)
