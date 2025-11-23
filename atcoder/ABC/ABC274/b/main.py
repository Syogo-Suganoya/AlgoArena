H, W = map(int, input().split())
C = [input().strip() for _ in range(H)]

# 転置して列ごとにまとめる
cols = list(zip(*C))  #

# '#' の数を数える
ans = [col.count("#") for col in cols]

# 出力
print(*ans)
