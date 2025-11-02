def kmp_search(text, pattern):
    # 前処理：部分一致テーブルを作る
    n, m = len(text), len(pattern)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    # 探索
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                return i - m + 1
    return -1


N = int(input())
for _ in range(N):
    A = input()
    B = input()

    # 2周分のAを作成
    double_A = A + A
    pos = kmp_search(double_A, B)

    # 位置チェック
    if pos == -1 or pos >= len(A):
        print(-1)
    else:
        print(pos)
