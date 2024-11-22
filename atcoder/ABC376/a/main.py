# 公式解説から引用
# https://atcoder.jp/contests/abc376/editorial/11190

n, c = map(int, input().split())
t = list(map(int, input().split()))
ans = 1
pre = t[0]
for i in range(1, n):
    if t[i] - pre >= c:
        ans += 1
        pre = t[i]

print(ans)
