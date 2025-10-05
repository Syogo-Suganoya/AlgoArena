T = int(input())
for _ in range(T):
    N = int(input())
    S = input()

    mx = [0, 0]  # 各文字 '0', '1' の最長連続長
    cnt = [0, 0]  # 各文字の合計出現数

    l = 0
    while l < N:
        r = l + 1
        while r < N and S[l] == S[r]:
            r += 1
        c = int(S[l])
        length = r - l
        mx[c] = max(mx[c], length)
        cnt[c] += length
        l = r

    ans = 2 * N
    for i in range(2):
        ans = min(ans, (cnt[i] - mx[i]) * 2 + cnt[i ^ 1])
    print(ans)
