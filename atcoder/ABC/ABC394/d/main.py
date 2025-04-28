def main(S):
    stack = []
    pair = {")": "(", "]": "[", ">": "<"}  # 閉じ括弧から対応する開き括弧を引く辞書

    for ch in S:
        if ch in "([<":
            # 開き括弧ならスタックに積む
            stack.append(ch)
        elif ch in ")]>":
            # 閉じ括弧が来たら対応をチェック
            if not stack:
                # スタックが空なら対応する開き括弧がない＝NG
                return False
            if stack[-1] != pair[ch]:
                # スタックの一番上と対応していない＝NG
                return False
            stack.pop()  # 正しく対応していればスタックから取り除く

    # 最後にスタックが空ならOK（全部きれいに対応できた）
    return not stack


S = input()
print("Yes" if main(S) else "No")
