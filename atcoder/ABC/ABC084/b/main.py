import re

A, B = map(int, input().split())
S = input()

# 正規表現パターンを組み立てる（\d は数字）
pattern = f"^\\d{{{A}}}-\\d{{{B}}}$"

# パターンにマッチするか判定
if re.match(pattern, S):
    print("Yes")
else:
    print("No")
