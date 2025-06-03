N, K = map(int, input().split())
A = list(map(int, input().split()))

# Aをソートした正解状態を保持
sorted_A = sorted(A)

# K個おきにインデックスを分割し、それぞれソートしてから元に戻す
# 例: K=2なら、A[0],A[2],...とA[1],A[3],...をそれぞれソート
groups = [[] for _ in range(K)]
for i in range(N):
    groups[i % K].append(A[i])

# 各グループを個別にソート
for g in groups:
    g.sort()

# 再構成した配列を作成
B = []
indices = [0] * K  # 各グループの読み出しインデックス
for i in range(N):
    group_id = i % K
    B.append(groups[group_id][indices[group_id]])
    indices[group_id] += 1

# 元の配列AをK個おきソートした結果と正解のソート済み配列を比較
if B == sorted_A:
    print("Yes")
else:
    print("No")
