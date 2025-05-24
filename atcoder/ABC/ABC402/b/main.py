Q = int(input())
stack = []

for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            X = query[1]
            stack.append(X)
        case 2:
            if stack:
                print(stack.pop(0))

"""
Q = int(input())

for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            X = query[1]
            Xをスタック
        case 2:
            ポップして出力
"""
