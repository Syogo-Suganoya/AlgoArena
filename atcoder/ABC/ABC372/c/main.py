N, Q = map(int, input().split())
S = list(input())

# 最初の "ABC" の数をカウント
l = set()
for i in range(N - 2):
    if S[i : i + 3] == ["A", "B", "C"]:
        l.add(i)


for _ in range(Q):
    X, C = input().split()
    X = int(X) - 1  # 0始まりに

    # 変更前に "ABC" だった箇所を確認して l から除外
    for i in range(3):
        idx = X - i
        if 0 <= idx <= N - 3 and idx in l:
            l.remove(idx)

    # 変更を適用
    S[X] = C

    # 変更後に "ABC" になった箇所を確認して l に加算
    for i in range(3):
        idx = X - i
        if 0 <= idx <= N - 3 and S[idx : idx + 3] == ["A", "B", "C"] and idx not in l:
            l.add(idx)

    print(len(l))
