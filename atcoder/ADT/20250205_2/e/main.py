N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = 10**18

ans = 0  # 最大の合計人数を記録
for x in range(max(Q) + 1):  # 料理Aを作る人数xを全探索
    y = INF  # 料理Bを作る人数yの上限値
    for i in range(N):
        if Q[i] < A[i] * x:  # x人分の料理Aを作るのに材料が足りない場合
            y = -INF  # 不可能なので y を無効な値にする
        elif B[i] > 0:  # 料理Bが材料を消費する場合
            y = min(y, (Q[i] - A[i] * x) // B[i])  # B を作れる最大人数を更新
    ans = max(ans, x + y)
print(ans)
