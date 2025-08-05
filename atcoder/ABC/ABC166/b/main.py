n, k = map(int, input().split())
v = [True] * n  # 最初は全員お菓子を受け取っていないとする

for _ in range(k):
    d = int(input())
    a_list = list(map(int, input().split()))
    for a in a_list:
        v[a - 1] = False  # お菓子を受け取った人を False にする

ans = 0
for i in range(n):
    if v[i]:
        ans += 1

print(ans)
