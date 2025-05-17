from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

sa = sum(A)
c = Counter(A)

for _ in range(Q):
    B, C = map(int, input().split())

    if B in c:
        cnt = c[B]  # B の出現回数
        # 総和から、B を全部取り除いて C をその個数分足す
        sa += (C - B) * cnt
        # C の個数を増やす
        c[C] += cnt
        # B の個数をゼロにする（すべて C に置き換えたので）
        c[B] = 0

    print(sa)
