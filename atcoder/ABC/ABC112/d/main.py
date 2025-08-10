def max_gcd(N, M):
    # M のすべての約数を列挙
    divisors = []
    i = 1
    while i * i <= M:
        if M % i == 0:
            divisors.append(i)
            if i * i != M:
                divisors.append(M // i)
        i += 1

    # 最大の d を探す
    ans = 1
    for d in divisors:
        if d * N <= M:
            ans = max(ans, d)
    return ans


# 入力読み込み
N, M = map(int, input().split())
print(max_gcd(N, M))
