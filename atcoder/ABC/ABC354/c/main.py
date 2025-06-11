N = int(input())
AC = [tuple(map(int, input().split())) + (i + 1,) for i in range(N)]  # (A, C, index)

AC.sort()  # Aで昇順ソート

stack = []

for a, c, idx in AC:
    # stackの後ろから見て、今のカードよりコストが高ければ削除
    while stack and stack[-1][1] > c:
        stack.pop()
    # 今のカードが既に強さで負けているものなら追加しない
    if not stack or stack[-1][0] != a:
        stack.append((a, c, idx))

ans = sorted(card[2] for card in stack)
print(len(ans))
print(*ans)
