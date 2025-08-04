N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

# 最初は青木くんが全村のAを取っている
aoki_total = sum(a for a, b in AB)

# 各村の impact を計算し、降順で並べる
impact_list = [2 * a + b for a, b in AB]
impact_list.sort(reverse=True)

count = 0
takahashi_gain = 0

for impact in impact_list:
    takahashi_gain += impact
    count += 1
    if takahashi_gain > aoki_total:
        print(count)
        break
