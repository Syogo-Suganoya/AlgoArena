Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

MAX = 100001
is_prime = [True] * MAX
is_prime[0] = is_prime[1] = False

# エラトステネスの篩による素数判定
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX, i):
            is_prime[j] = False

# 「2017に似た数」の累積和
like2017 = [0] * MAX
for i in range(1, MAX):
    like2017[i] = like2017[i - 1]
    if i % 2 == 1 and is_prime[i] and is_prime[(i + 1) // 2]:
        like2017[i] += 1

# クエリの処理
for l, r in queries:
    print(like2017[r] - like2017[l - 1])
