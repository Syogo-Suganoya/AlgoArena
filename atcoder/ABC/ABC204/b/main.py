N = int(input())
A = list(map(int, input().split()))

# 各要素から10を引いた後、自然数のみ抽出
B = [a - 10 for a in A if a - 10 > 0]

# 合計を出力
print(sum(B))
