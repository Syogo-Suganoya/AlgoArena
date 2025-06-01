N = int(input())
res = 0

for i in range(1, N):
    # i の約数の個数を数える
    a_cnt = 0
    for j in range(1, int(i**0.5) + 1):
        if i % j == 0:
            a_cnt += 1
            if j != i // j:
                a_cnt += 1

    # N - i の約数の個数を数える
    b_cnt = 0
    ni = N - i
    for j in range(1, int(ni**0.5) + 1):
        if ni % j == 0:
            b_cnt += 1
            if j != ni // j:
                b_cnt += 1

    # 組み合わせの積を加算
    res += a_cnt * b_cnt

print(res)
