from collections import Counter

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    # 1. すべて同じ値なら Yes
    if all(a == A[0] for a in A):
        print("Yes")
        continue

    # 2. 先頭とその -1 倍しかなく、かつ個数が ceil/floor なら Yes
    cnt = Counter(A)
    keys = list(cnt.keys())
    if len(keys) == 2 and keys[0] == -keys[1]:
        p_cnt = cnt[keys[0]]
        n_cnt = cnt[keys[1]]
        if min(p_cnt, n_cnt) == N // 2:
            print("Yes")
            continue

    # 3. 絶対値の降順にソートして、等比かチェック
    A.sort(key=abs, reverse=True)
    ok = True
    for i in range(N - 2):
        if A[i] * A[i + 2] != A[i + 1] * A[i + 1]:
            ok = False
            break

    print("Yes" if ok else "No")
