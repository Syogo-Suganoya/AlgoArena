S = input()  # 入力文字列

stack = []  # 文字を積み上げるスタックを初期化

for ch in S:
    stack.append(ch)  # 1文字ずつスタックに積む

    # スタックの末尾3文字が "ABC" なら削除
    if len(stack) >= 3 and stack[-3:] == ["A", "B", "C"]:
        # 末尾の3文字を取り除く（逆順に pop）
        stack.pop()
        stack.pop()
        stack.pop()

# 最終的に残ったスタックの内容を結合して出力
print("".join(stack))
