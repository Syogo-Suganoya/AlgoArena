import math

a, b = input().split()


def is_square(n):
    root = int(math.isqrt(n))
    return root * root == n


def main():
    s = int(a + b)
    return is_square(s)


print("Yes" if main() else "No")
