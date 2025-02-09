ans = []

# 2 〜 1023 (2^10 - 1) のビットをチェック
for i in range(2, 1 << 10):
    x = 0
    for j in range(9, -1, -1):  # j = 9 から 0 まで降順ループ
        if i & (1 << j):  # jビット目が立っていたら
            x = x * 10 + j  # 数字を構築
    ans.append(x)

ans.sort()  # 数値を昇順ソート

# K 番目の数を取得
K = int(input())
print(ans[K - 1])
