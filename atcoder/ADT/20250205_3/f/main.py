N, Q = map(int, input().split())
S = list(input())


def count_abc_change(X):
    change = 0
    for k in range(3):
        idx = X - k  # 変更後に "ABC" が新たにできる可能性のある開始位置
        if 0 <= idx and idx + 2 < N:
            if "".join(S[idx : idx + 3]) == "ABC":
                change += 1
    return change


ans = "".join(S).count("ABC")
for _ in range(Q):
    X, C = input().split()
    X = int(X) - 1
    ans -= count_abc_change(X)
    S[X] = C
    ans += count_abc_change(X)
    print(ans)
