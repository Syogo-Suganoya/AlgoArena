N = int(input())
A = list(map(int, input().split()))

# 座標圧縮のためにソート＆辞書化
sorted_unique = sorted(set(A))  # 重複を除いてソート
compress_dict = {value: i + 1 for i, value in enumerate(sorted_unique)}  # 1-indexed

# 元のAを座標圧縮後の値に置き換え
compressed = [compress_dict[a] for a in A]

print(*compressed)
