from collections import Counter

N, M = map(int, input().split())

cnt = Counter()
for _ in range(N):
    K, *A = map(int, input().split())
    cnt.update(A)  # A の要素をカウントに加算

# すべての行に出てきた数字の個数を数える
ans = sum(1 for v in cnt.values() if v == N)
print(ans)
