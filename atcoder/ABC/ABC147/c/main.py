N = int(input())

# 各人の証言を保持
# testimonies[i] = [(x, y), (x, y), ...]
#  i番目の人が x さんは正直(y=1)／不親切(y=0) と証言している
testimonies = []
for _ in range(N):
    A = int(input())
    temp = []
    for _ in range(A):
        x, y = map(int, input().split())
        temp.append((x - 1, y))  # 0-index に直す
    testimonies.append(temp)

ans = 0  # 最大の正直者人数を記録

# 各人が正直(1) or 不親切(0) かを全探索 (2^N通り)
for mask in range(1 << N):
    ok = True  # この仮定が矛盾なく成り立つかどうか
    for i in range(N):
        # maskのiビット目が1 → i番目の人を正直者と仮定
        if not (mask >> i) & 1:
            continue
        # i番目が正直なら、その証言はすべて真実である必要がある
        for x, y in testimonies[i]:
            # x番目の人の実際の仮定（maskで決まる）
            if ((mask >> x) & 1) != y:
                ok = False
                break
        if not ok:
            break
    if ok:
        # 矛盾がなければ、この仮定の正直者数をカウント
        honest_count = bin(mask).count("1")
        ans = max(ans, honest_count)

print(ans)
