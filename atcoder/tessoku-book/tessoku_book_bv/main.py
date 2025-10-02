# N: 盤面のサイズ
N = int(input())
# P: N×N の盤面の入力
P = [list(map(int, input().split())) for _ in range(N)]

# vertical, horizontal はそれぞれ列・行の先頭にある0以外の数字を格納するリスト
vertical = []
horizontal = []

# 各行の先頭にある0でない数字を vertical に追加
for i in range(N):
    for j in range(N):
        if P[i][j] != 0:
            vertical.append(P[i][j])
            break  # 先頭の非0だけなのでループを抜ける

# 各列の先頭にある0でない数字を horizontal に追加
for i in range(N):
    for j in range(N):
        if P[j][i] != 0:
            horizontal.append(P[j][i])
            break  # 先頭の非0だけなのでループを抜ける

# vertical を昇順に揃えるための操作回数
ver_con = 0
for num in range(1, N + 1):
    for i in range(N):
        if vertical[i] == num:
            idx = i
            # num を正しい位置までスワップで移動
            while idx + 1 != num:
                vertical[idx], vertical[idx - 1] = vertical[idx - 1], vertical[idx]
                ver_con += 1
                idx -= 1

# horizontal を昇順に揃えるための操作回数
hor_con = 0
for num in range(1, N + 1):
    for i in range(N):
        if horizontal[i] == num:
            idx = i
            # num を正しい位置までスワップで移動
            while idx + 1 != num:
                horizontal[idx], horizontal[idx - 1] = (
                    horizontal[idx - 1],
                    horizontal[idx],
                )
                hor_con += 1
                idx -= 1

# 最終的な操作回数 = 行の操作回数 + 列の操作回数
ans = ver_con + hor_con
print(ans)
