from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# 末尾2桁ごとの出現回数
mod_count = defaultdict(int)
ans = 0

# 逆からループすることで「i以降」の要素を先に数える
for a in reversed(A):
    m = a % 100
    complement = (100 - m) % 100  # 100 ちょうどの場合も 0 に
    ans += mod_count[complement]
    mod_count[m] += 1

print(ans)
