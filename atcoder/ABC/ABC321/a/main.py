N = input().strip()

# 文字列Nの重複判定
is_unique = len(set(N)) == len(N)

# 降順判定
is_descending = list(N) == sorted(N, reverse=True)

if is_unique and is_descending:
    print("Yes")
else:
    print("No")
