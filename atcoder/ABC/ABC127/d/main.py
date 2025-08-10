N, M = map(int, input().split())
A = list(map(int, input().split()))

BC = []
for _ in range(M):
    B, C = map(int, input().split())
    BC.append((C, B))  # C を先にしてソートしやすくする

# A を昇順、BC を C の降順にソート
A.sort()
BC.sort(reverse=True)

idx = 0  # A のどこまで置き換えたか
for c, b in BC:
    for _ in range(b):
        if idx < N and A[idx] < c:
            A[idx] = c
            idx += 1
        else:
            # out of range
            break

print(sum(A))
