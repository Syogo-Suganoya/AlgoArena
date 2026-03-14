import sys

sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))

g = [[] for _ in range(N)]
for _ in range(N - 1):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    g[U].append(V)
    g[V].append(U)

ans = ["No"] * N
count = {}


def dfs(cur, par, flg):
    if count.get(A[cur], 0) > 0:
        flg = True

    if flg:
        ans[cur] = "Yes"

    count[A[cur]] = count.get(A[cur], 0) + 1

    for next in g[cur]:
        if next != par:
            dfs(next, cur, flg)

    count[A[cur]] -= 1
    if count[A[cur]] == 0:
        del count[A[cur]]


dfs(0, -1, False)

for x in ans:
    print(x)
