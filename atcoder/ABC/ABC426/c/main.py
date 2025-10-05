N, Q = map(int, input().split())
pc = [0] + [1] * N  # pc[0]=0, pc[1..n]=1
o = 1  # 現在処理済みの位置

for _ in range(Q):
    X, Y = map(int, input().split())
    res = 0
    while o <= X:
        res += pc[o]
        pc[Y] += pc[o]
        o += 1
    print(res)
