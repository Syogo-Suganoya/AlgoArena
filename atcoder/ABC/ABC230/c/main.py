N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

# 出力範囲内の各マスを処理
for i in range(P, Q + 1):
    row = ""
    for j in range(R, S + 1):
        # 条件1: i - j == A - B
        if i - j == A - B:
            row += "#"
        # 条件2: i + j == A + B
        elif i + j == A + B:
            row += "#"
        else:
            row += "."
    print(row)
