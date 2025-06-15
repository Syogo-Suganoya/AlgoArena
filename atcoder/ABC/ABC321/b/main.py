N, X = map(int, input().split())  # N: 数列の長さ、X: 目標となる合計
A = list(map(int, input().split()))  # A: 最初のN-1個の点数
A.append(-1)  # 未定の1人分として、仮で -1 を追加しておく

# 最後の1人の点数を 0〜100 で全探索
for last in range(0, 101):
    B = A.copy()  # Aのコピー（元を壊さないように）
    B[N - 1] = last  # 最後の1人の点数を仮にlastとする
    B.sort()  # 最小・最大を除くためにソート

    sum_middle = 0
    for i in range(1, N - 1):  # 最小と最大を除いた要素の合計を計算
        sum_middle += B[i]

    if sum_middle >= X:
        print(last)  # 条件を満たしたらその値を出力
        exit()  # 処理終了

# どの値でも条件を満たせなかった場合
print("-1")
