N, M = map(int, input().split())

div1 = (1600, 2799)
div2 = (1200, 2399)

rate = M

for _ in range(N):
    D, A = map(int, input().split())
    if D == 1:
        if div1[0] <= rate <= div1[1]:
            rate += A
    if D == 2:
        if div2[0] <= rate <= div2[1]:
            rate += A

print(rate)
