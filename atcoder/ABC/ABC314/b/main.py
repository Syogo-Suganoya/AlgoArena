N = int(input())
bags = []  # 各袋のデータをまとめておく
for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    bags.append(A)

X = int(input())

res = []
min_len = float("inf")

for i, A in enumerate(bags, 1):  # 1-indexで出力するため1から
    if X not in A:
        continue
    if len(A) < min_len:
        res = [i]
        min_len = len(A)
    elif len(A) == min_len:
        res.append(i)

print(len(res))
print(*res)
