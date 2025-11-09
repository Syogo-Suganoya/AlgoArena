S = input()  # 入力文字列
ans = []  # 出力用リスト
flag = False  # 状態管理フラグ

for ch in S:
    if ch == "#":
        # '#' はそのまま出力
        ans.append("#")
        # フラグをリセット
        flag = False
    else:
        # '.' の処理
        if flag:
            ans.append(".")
        else:
            ans.append("o")
            flag = True

# 結果を文字列にして出力
print("".join(ans))
