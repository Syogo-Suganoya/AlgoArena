import math

N = int(input())
C, S, F = [], [], []

for _ in range(N - 1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(N):
    t = 0
    for j in range(i, N - 1):
        if t < S[j]:
            # 出発開始時刻まで待つ
            t = S[j]
        else:
            # 次の列車の出発時刻まで待つ
            # t以上のFの倍数を算出
            if t % F[j] != 0:
                t = math.ceil(t / F[j]) * F[j]
        t += C[j]
    print(t)
