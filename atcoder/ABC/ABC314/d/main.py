N = int(input())
S = list(input())
Q = int(input())
TXC = [list(input().split()) for _ in range(Q)]

# クエリを後ろから見て、2か3のラストを記録
li = -1
for i in range(Q - 1, -1, -1):
    t, x, c = TXC[i]
    t = int(t)
    if t == 2 or t == 3:
        li = i
        break

# クエリ実行
for i, ts in enumerate(TXC):
    t, x, c = ts
    t = int(t)
    if t == 1:
        x = int(x) - 1
        S[x] = c
    elif t == 2 and i == li:
        S = [ch.lower() for ch in S]
    elif t == 3 and i == li:
        S = [ch.upper() for ch in S]

print("".join(S))
