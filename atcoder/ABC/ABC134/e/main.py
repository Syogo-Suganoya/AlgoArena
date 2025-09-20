import bisect

N = int(input())
A = [int(input()) for _ in range(N)]

# 各列の末尾（降順列なので -1 を掛けて昇順として管理）
ends = []

for a in A:
    a = -a  # 値を反転
    i = bisect.bisect_right(ends, a)
    if i < len(ends):
        ends[i] = a
    else:
        ends.append(a)

print(len(ends))
