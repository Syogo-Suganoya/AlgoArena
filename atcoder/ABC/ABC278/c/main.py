from collections import defaultdict

# 入力の読み込み
N, Q = map(int, input().split())
follow = defaultdict(set)

for _ in range(Q):
    T, A, B = map(int, input().split())
    match T:
        case 1:
            follow[A].add(B)
        case 2:
            follow[A].discard(B)
        case 3:
            if B in follow[A] and A in follow[B]:
                print("Yes")
            else:
                print("No")
