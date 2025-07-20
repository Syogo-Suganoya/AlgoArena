N = int(input())
A = list(map(int, input().split()))

# vol[i]：i巻が1冊あるかどうか（1-indexedでN+2まで）
vol = [False] * (N + 2)
sold = 0  # 売れる冊数（重複や大きすぎる巻）

for a in A:
    if a >= len(vol):
        sold += 1  # 不要な巻（大きすぎ）
    elif vol[a]:
        sold += 1  # 重複巻
    else:
        vol[a] = True  # はじめての巻 → キープ

L = 1
R = N + 1

while True:
    # L: 次に読みたい巻
    while L < len(vol) and vol[L]:
        L += 1
    # R: 末尾で余ってる巻（読めるけど不要）
    while R > 0 and not vol[R]:
        R -= 1

    if sold >= 2:
        sold -= 2
        vol[L] = True
    else:
        if L >= R:
            break
        vol[R] = False
        sold += 1

print(L - 1)
