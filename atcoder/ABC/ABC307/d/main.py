n = int(input())
s = list(input())

stack = []
cnt = 0

for c in s:
    if c == "(":
        cnt += 1  # 左カッコが来たらカウント
    elif c == ")" and cnt > 0:
        cnt -= 1  # 対応する左カッコがある場合だけペアを消す
        # 直前の "(" まで pop して取り除く
        while True:
            p = stack.pop()
            if p == "(":
                break
        continue
    stack.append(c)

print("".join(stack))
