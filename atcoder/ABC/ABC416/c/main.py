N, K, X = map(int, input().split())
S = [input().strip() for _ in range(N)]

results = []


def dfs(cur, depth):
    if depth == K:
        results.append(cur)
        return
    for s in S:
        dfs(cur + s, depth + 1)


dfs("", 0)
results.sort()
print(results[X - 1])
