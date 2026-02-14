N, M = map(int, input().split())


def digit_sum(x):
    return sum(map(int, str(x)))


count = 0
for i in range(1, N + 1):
    if digit_sum(i) == M:
        count += 1

print(count)
