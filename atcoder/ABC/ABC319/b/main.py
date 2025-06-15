N = int(input())

# 1〜9 のうち、N の約数（N を割り切れる数）だけをリストアップしておく
divs = [j for j in range(1, 10) if N % j == 0]

ans = []

# 0 から N までの各位置 i に対して判定を行う
for i in range(N + 1):
    ch = "-"  # デフォルトは '-' にしておく
    for j in divs:
        if i % (N // j) == 0:  # i が N//j の倍数であるかを判定
            ch = str(j)
            break  # 最小の j を採用するので、見つかったらループを抜ける
    ans.append(ch)

print("".join(ans))
