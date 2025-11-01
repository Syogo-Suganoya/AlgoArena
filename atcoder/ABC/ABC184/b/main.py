N, X = map(int, input().split())
S = input()

# 命令列を1文字ずつ処理
for cmd in S:
    if cmd == "o":
        X += 1  # "o" の場合は X を1増やす
    elif cmd == "x":
        X = max(0, X - 1)  # "x" の場合は X を1減らす。ただし0未満にはしない

print(X)
