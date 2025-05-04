T = input()  # 目標の文字列
N = int(input())  # 袋の数

# 各袋に含まれる文字列リスト（2番目以降が文字列のリスト）
bags = [input().split()[1:] for _ in range(N)]

INF = float("inf")  # 十分に大きい数（無限大の代わり）

# dp[i][j] := i個目の袋まで使って、Tのj文字目まで一致させるのに必要な最小コスト
dp = [[INF] * (len(T) + 1) for _ in range(N + 1)]
dp[0][0] = 0  # 初期状態（何も選ばず、0文字一致、コスト0）

# 各袋についてループ
for i in range(N):
    for j in range(len(T) + 1):
        # 遷移1: i番目の袋を何も使わずスキップ
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

        # 遷移2: i番目の袋の中の各文字列を選ぶ場合
        for s in bags[i]:
            # Tのj文字目以降がsで始まるなら使える
            if T.startswith(s, j):
                # sの分だけjを進める
                dp[i + 1][j + len(s)] = min(dp[i + 1][j + len(s)], dp[i][j] + 1)

# 最後に、T全体と一致するための最小コストを取得
ans = dp[N][len(T)]
# 解が存在するなら出力、なければ -1
print(ans if ans != INF else -1)
