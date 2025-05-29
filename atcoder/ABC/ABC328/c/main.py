N, Q = map(int, input().split())
S = input()

# c[i]: 先頭からi文字目までに「連続する同じ文字」が何回あったか
c = [0] * (N + 1)

for i in range(1, N):
    c[i + 1] = c[i]
    if S[i] == S[i - 1]:
        c[i + 1] += 1

for _ in range(Q):
    l, r = map(int, input().split())
    # 区間[l, r]の範囲内での「前と同じ文字」の数を出力
    print(c[r] - c[l])
