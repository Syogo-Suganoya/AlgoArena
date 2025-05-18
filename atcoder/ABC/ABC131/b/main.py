N, L = map(int, input().split())

# 長さ N のリストを作成（L から L+N-1 まで）
A = [L + i for i in range(N)]

# 絶対値が最小の要素を取り除く
A.remove(min(A, key=abs))

# 残った要素の合計を出力
print(sum(A))
