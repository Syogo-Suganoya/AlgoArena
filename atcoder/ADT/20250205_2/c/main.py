N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = []
i = j = 1

while i <= N:
    while j in A:
        j += 1

    for k in range(j, i - 1, -1):  # i から j まで逆順で追加
        ans.append(k)

    i = j + 1  # 次の区間の開始位置へ
    j += 1  # jも進める

print(*ans)
