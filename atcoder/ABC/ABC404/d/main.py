# 入力
N, M = map(int, input().split())  # N:動物園の数, M:動物の種類
C = list(map(int, input().split()))  # 各動物園の入園料

# G[i] = 動物園 i で見られる動物のリスト
G = [[] for i in range(N)]
for i in range(M):
    v = list(map(int, input().split()))[1:]  # 最初の数字は動物の数なので除外
    for e in v:
        G[e - 1].append(i)  # 動物 e が見られる動物園に i を追加

ans = 1e18  # 最小コストの初期化

# 2^N ではなく 2N ビットで全探索（動物園を 0,1 回として選択する場合を表現）
for S in range(1 << (2 * N)):
    cnt = [0] * M  # 各動物が何回見られるかのカウント
    cost = 0  # 現在の組み合わせの合計コスト

    for i in range(2 * N):
        if S >> i & 1:  # i 番目のビットが 1 なら動物園 i//2 を訪問
            for e in G[i // 2]:
                cnt[e] += 1  # 動物 e を見た回数を増やす
            cost += C[i // 2]  # 動物園のコストを加算

    # 全ての動物が少なくとも 2 回見られる場合、最小コストを更新
    if min(cnt) >= 2:
        ans = min(ans, cost)

print(ans)
