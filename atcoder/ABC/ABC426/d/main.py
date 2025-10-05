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
        mx[c] = max(mx[c], length)  # 文字 c の最長連続長を更新
        cnt[c] += length  # 文字 c の総出現数
        l = r

    ans = 2 * N
    for i in range(2):
        # i = 0 または 1 を全て揃える場合の操作回数を計算
        # (cnt[i] - mx[i]) → 長さが揃わない部分を移動
        # 2倍するのは両端から操作可能だから
        # cnt[i ^ 1] → 揃えたい文字以外の文字を動かす必要
        ans = min(ans, (cnt[i] - mx[i]) * 2 + cnt[i ^ 1])
    print(ans)
