N, M = map(int, input().split())
S = input().strip()
T = input().strip()

# prefix 判定：T の先頭 N 文字と一致？
is_prefix = T[:N] == S

# suffix 判定：T の末尾 N 文字と一致？
is_suffix = T[-N:] == S

# 結果を出力
if is_prefix and is_suffix:
    print(0)
elif is_prefix:
    print(1)
elif is_suffix:
    print(2)
else:
    print(3)
