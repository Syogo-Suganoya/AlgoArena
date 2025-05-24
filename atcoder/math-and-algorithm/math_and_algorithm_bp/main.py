N = int(input())


def main():
    stack = []  # 括弧の対応を確認するためのスタック（LIFO）

    for char in S:  # 入力文字列を左から1文字ずつ確認
        if char == "(":
            # 開き括弧が来たら、対応する閉じ括弧を待つためにスタックに積む
            stack.append(char)
        elif char == ")":
            # 閉じ括弧が来たら、スタックの上に対応する開き括弧があるか確認
            if not stack:
                # スタックが空なら、対応する開き括弧がない＝不正な括弧列
                return False
            # 対応する開き括弧を取り出す（削除する）
            stack.pop()

    # 最後にスタックが空なら、すべての括弧が対応している＝正しい括弧列
    return not stack


S = input()
print("Yes" if main() else "No")
