N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

res = 0  # 最終的な満足度の合計
bef = None  # 直前に食べた料理の番号（0-indexed）

for i in range(N):
    dish = A[i] - 1  # A[i]は1-indexedなので0-indexedに直す
    res += B[dish]  # 通常の満足度を加算
    if bef is not None and dish - bef == 1:
        res += C[bef]  # 直前の料理と連番なら、追加満足度も加算
    bef = dish  # 現在の料理を次回のために記録

print(res)  # 合計満足度を出力
