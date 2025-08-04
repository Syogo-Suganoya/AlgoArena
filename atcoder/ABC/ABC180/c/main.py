N = int(input())

divisors = set()
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        divisors.add(i)
        divisors.add(N // i)

# 昇順に出力
for d in sorted(divisors):
    print(d)
