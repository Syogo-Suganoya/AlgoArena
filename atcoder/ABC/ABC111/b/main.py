N = int(input())

# N から 999 までで、最初に 111 の倍数のものを出力
for x in range(N, 1000):
    if x % 111 == 0:
        print(x)
        break
