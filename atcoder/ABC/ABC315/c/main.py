N = int(input())
d = {}

for _ in range(N):
    F, S = map(int, input().split())
    if F not in d:
        d[F] = []
    d[F].append(S)
    d[F].sort(reverse=True)
    if len(d[F]) > 2:
        d[F] = d[F][:2]


# 同じ味から2つ選ぶ
same = -1

# 異なる味から選ぶ
diff_list = []
diff = -1
for v in d.values():
    tmp = v[0]
    if len(v) == 2:
        tmp += v[1] / 2
    same = max(same, tmp)
    diff_list.append((max(v)))

diff_list.sort(reverse=True)
diff = diff_list[0]
if len(diff_list) >= 2:
    diff += diff_list[1]

print(int(max(same, diff)))
