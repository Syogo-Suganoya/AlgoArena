A, B, C, D = map(int, input().split())

diff = C * D - B
if 0 >= diff:
    print(-1)
else:
    print((A + diff - 1) // diff)
