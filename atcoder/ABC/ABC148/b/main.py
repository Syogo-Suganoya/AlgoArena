# 入力
N = int(input())
S, T = input().split()

# SとTを一文字ずつ取り出して交互に結合
for s_char, t_char in zip(S, T):
    print(s_char + t_char, end="")  # 改行せずに出力
