from sympy.ntheory import factorint

N = int(input())
A = list(map(int, input().split()))

count = 0

for a in A:
    # 素因数分解
    factors = factorint(a)

    # 2 の因数があれば、その指数を加算
    if 2 in factors:
        count += factors[2]

print(count)
