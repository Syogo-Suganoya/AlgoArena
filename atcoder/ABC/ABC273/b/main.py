X, K = map(int, input().split())

from decimal import ROUND_HALF_UP, Decimal


def round_half_up(n, digits=0):
    exponent = Decimal("1e{}".format(-digits))
    return float(Decimal(n).quantize(exponent, rounding=ROUND_HALF_UP))


for i in range(K):
    X = round_half_up(X, -(i + 1))
print(int(X))
