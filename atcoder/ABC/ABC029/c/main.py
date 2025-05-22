from itertools import product

N = int(input())

# a, b, c から N 回選んだ直積（つまり全通り）
for p in product("abc", repeat=N):
    print("".join(p))  # タプルを文字列にして出力
