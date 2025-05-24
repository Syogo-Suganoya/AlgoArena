def sol(a, b, c):
    """
    2次方程式 a*x^2 + b*x + c <= 0 となる最大の整数 x を二分探索で求め、
    その後、a*x^2 + b*x + c == 0 か判定する。
    """
    l, r = 0, 600000001
    while r - l > 1:
        mid = (l + r) // 2
        if a * mid * mid + b * mid + c <= 0:
            l = mid
        else:
            r = mid
    if a * l * l + b * l + c == 0:
        return l
    return -1


def main():
    n = int(input())
    d = 1
    while d * d * d <= n:
        if n % d == 0:
            m = n // d  # 3*k^2 + 3*d*k + d^2 = m
            k = sol(3, 3 * d, d * d - m)
            if k > 0:
                print(k + d, k)
                return
        d += 1
    print(-1)


if __name__ == "__main__":
    main()
