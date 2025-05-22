from collections import Counter

N = int(input())
A = list(map(int, input().split()))

res = 0

# 各値が何回出てきたかをカウント
c = Counter(A)

# 各値に対して処理
for count in c.values():
    if count < 3:
        continue  # 3つ未満ではnC3は0なので無視

    # nC3 = n * (n-1) * (n-2) // 6 を計算
    res += count * (count - 1) * (count - 2) // 6

print(res)

"""
N = int(input())
A = list(map(int, input().split()))
res=0
c=Counter(A)
for a in c.velues():
    aが2以下なら
        continue
    res=aC3を算出
print(res)
"""
