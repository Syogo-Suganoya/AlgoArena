X, N = map(int, input().split())
A = set(map(int, input().split())) if N > 0 else set()  # 禁止リストを集合に

# 差が小さい順に探索
for d in range(101):  # X の範囲が ±100 以内で答えが見つかる保証あり
    if X - d not in A:
        print(X - d)
        break
    if X + d not in A:
        print(X + d)
        break
