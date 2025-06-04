N, X = map(int, input().split())
S = input()


# ノード関係を定義する関数
def parent(now):
    return now // 2


def left(now):
    return now * 2


def right(now):
    return now * 2 + 1


# 圧縮処理：スタックで命令を詰めて相殺
stack = []

for ch in S:
    if ch == "U":
        if stack and stack[-1] in ("L", "R"):
            stack.pop()  # 子→親の往復を相殺
        else:
            stack.append("U")
    else:
        stack.append(ch)  # LまたはRはそのまま追加

# 圧縮された命令列に従って now を更新
now = int(X)

for ch in stack:
    if ch == "U":
        now = parent(now)
    elif ch == "L":
        now = left(now)
    elif ch == "R":
        now = right(now)

print(now)
