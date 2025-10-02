n = int(input())
a = [0] + list(map(int, input().split()))  # 先頭にダミーの0を追加

ans = [-1] * (n + 1)  # 各日の答えを格納
stack = []  # 株価が大きい日を保持

# 1日目から順に処理
for i in range(1, n + 1):
    # 今日より株価が低い日は、将来の比較には不要なのでスタックから除去
    while stack and a[stack[-1]] < a[i]:
        stack.pop()

    # スタックが残っていれば、そのトップが「直近で自分より株価が高い日」
    if stack:
        ans[i] = stack[-1]  # 日付（インデックス）を記録

    # 今日をスタックに追加（将来の日のために使える候補）
    stack.append(i)

# 1日目からn日目までの答えを出力
print(*ans[1:])
