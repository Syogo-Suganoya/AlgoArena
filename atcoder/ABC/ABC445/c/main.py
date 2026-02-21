N = int(input())
A = list(map(int, input().split()))
K = 10**100

used = [False] * N
res = [0] * N

for i in range(N):
    if used[i]:
        continue

    path = []
    pos = {}
    now = i
    step = 0

    while True:
        if used[now]:
            final = res[now]
            for node in reversed(path):
                final = A[node] - 1
                res[node] = res[final]
                used[node] = True
            break

        if now in pos:
            loop_l = pos[now]
            loop = path[loop_l:]
            loop_len = len(loop)

            for j in range(loop_len):
                target = loop[(j + K) % loop_len]
                res[loop[j]] = target
                used[loop[j]] = True

            for node in reversed(path[:loop_l]):
                res[node] = res[A[node] - 1]
                used[node] = True
            break

        pos[now] = step
        path.append(now)
        now = A[now] - 1
        step += 1

for i in range(N):
    print(res[i] + 1)
