N, M = map(int, input().split())
a = []
for _ in range(M):
    c, *lst = map(int, input().split())
    if len(lst) < c:
        lst += list(map(int, input().split()))
    a.append(lst)

ans = 0
for b in range(1 << M):  # 全ての選び方（2^M通り）を列挙
    s = set()
    for i in range(M):
        if (b >> i) & 1:
            s.update(a[i])  # 集合に追加
    if len(s) == N:  # 1〜N すべてが含まれているか？
        ans += 1

print(ans)


def anoter():
    """
    別解
    combinationsで組み合わせ網羅
    """
    from itertools import combinations

    N, M = map(int, input().split())
    a = []
    for _ in range(M):
        c, *lst = map(int, input().split())
        if len(lst) < c:
            lst += list(map(int, input().split()))
        a.append(lst)

    ans = 0
    for k in range(1, M + 1):  # 1個〜M個の箱の選び方すべてを試す
        for comb in combinations(a, k):
            s = set()
            for group in comb:
                s.update(group)
            if len(s) == N:
                ans += 1

    print(ans)
