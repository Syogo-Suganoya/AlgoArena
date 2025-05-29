def to_base_n(n, base):
    """
    10進数をN進数にする
    """
    res = []
    while n > 0:
        res.append(str(n % base))
        n //= base
    return "".join(res[::-1])


N = int(input())
if N == 1:
    print(0)
    exit()
print(int(to_base_n(N - 1, 5)) * 2)
