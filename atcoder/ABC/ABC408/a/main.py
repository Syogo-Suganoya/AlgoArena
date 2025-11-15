N, S = map(int, input().split())
T = list(map(int, input().split()))

# 先頭に 0 秒を追加して、最初の叩きからの差を簡単に扱う
T = [0] + T

# 判定
for i in range(1, N + 1):
    if T[i] - T[i - 1] > S:
        print("No")
        break
else:
    print("Yes")
