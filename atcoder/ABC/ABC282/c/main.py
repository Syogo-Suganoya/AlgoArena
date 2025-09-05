N = int(input())
S = input().strip()

result = []
inside = False  # ダブルクォーテーションの内側かどうか

for c in S:
    if c == '"':
        inside = not inside  # 内外を切り替える
        result.append(c)
    else:
        if not inside and c == ",":
            result.append(".")  # 外側のカンマだけ置換
        else:
            result.append(c)  # それ以外はそのまま

print("".join(result))
