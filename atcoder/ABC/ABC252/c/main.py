n = int(input())
s = [input() for _ in range(n)]

ans = float("inf")

# 0〜9のどの数字を揃えるか全探索
for target in range(10):
    time_count = [0] * 1000  # 各時刻にその数字が止められる回数（上限多めに取っておく）

    # 各スロットに対して、その数字が何秒目に出てくるかを記録
    for i in range(n):
        for t in range(10):  # 各リールの0〜9の位置
            if s[i][t] == str(target):
                time_count[t] += 1  # 時刻 t に数字 target が出現する

    # 貪欲に、同じ位置に複数あれば10秒ごとにずらす
    max_time = 0
    for t in range(10):
        if time_count[t] > 0:
            last_time = t + 10 * (time_count[t] - 1)
            max_time = max(max_time, last_time)

    ans = min(ans, max_time)

print(ans)
