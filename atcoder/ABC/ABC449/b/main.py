H, W, Q = map(int, input().split())

cw = W
ch = H
for i in range(Q):
    t, RC = map(int, input().split())
    if t == 1:
        print(RC * cw)
        ch -= RC

    if t == 2:
        print(RC * ch)
        cw -= RC
