N = int(input())


def sum_range(a, n):
    return n * (2 * a + (n - 1)) // 2


res = 0
for i in range(N):
    A, B = map(int, input().split())
    res += sum_range(A, B - A + 1)
print(res)
