from collections import deque

N, M = map(int, input().split())
S = list(input())
T = input()

checked = [False] * (N - M + 1)
q = deque()


def check(i):
    if checked[i]:
        return
    ok = True
    for j in range(M):
        if S[i + j] != T[j] and S[i + j] != "#":
            ok = False
            break
    if ok:
        checked[i] = True
        q.append(i)


for i in range(N - M + 1):
    check(i)

while q:
    i = q.popleft()
    for j in range(M):
        S[i + j] = "#"
    for k in range(max(0, i - M + 1), min(N - M + 1, i + M)):
        check(k)

print("Yes" if all(c == "#" for c in S) else "No")
