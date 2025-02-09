import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 各 K グループの累積和を格納するリスト
R = [[0] * (N + 1) for _ in range(K)]  # 各 K グループごとの累積和を管理

# 各要素を K グループに分けて累積和を構築
for i in range(N):
    R[i % K][i + 1] += A[i]  # i 番目の値を (i % K) 番目のグループに格納

# 各 K グループについて累積和を計算
for i in range(K):
    R[i] = list(itertools.accumulate(R[i]))  # 各グループの累積和を計算

# クエリ処理
Q = int(input())  # クエリの数
for _ in range(Q):
    l, r = map(int, input().split())  # クエリで与えられる範囲 [l, r]
    S = set()  # 各グループの部分和を格納する集合

    # 各 K グループの部分和を求める
    for i in range(K):
        S.add(R[i][r] - R[i][l - 1])  # 各グループの部分和をセットに追加

    # すべてのグループの部分和が同じなら "Yes", 異なるなら "No"
    if len(S) == 1:
        print("Yes")
    else:
        print("No")
