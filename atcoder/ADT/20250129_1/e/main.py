import sys

# 入力
N, S = sys.stdin.readlines()

# S をダブルクオートで分割
separated = S.split('"')

# 偶数番目（0-indexed）の部分だけカンマをピリオドに置換
for i in range(0, len(separated), 2):
    separated[i] = separated[i].replace(",", ".")

# 連結して出力
print('"'.join(separated))
