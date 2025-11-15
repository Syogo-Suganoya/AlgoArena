N = int(input())
A = list(map(int, input().split()))

# 重複を消してユニークな値だけにする
unique = set(A)

# ソートして小さい順のリストに戻す
sorted_unique = sorted(unique)

# 出力
print(len(sorted_unique))
print(*sorted_unique)
