from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)

# 2本以上の長さを抽出して降順ソート
pairs = [k for k in c if c[k] >= 2]
pairs.sort(reverse=True)

# 4本以上の長さがあれば正方形も候補になる
square = [k for k in c if c[k] >= 4]
square.sort(reverse=True)

res = 0
if len(pairs) >= 2:
    res = max(res, pairs[0] * pairs[1])
if square:
    res = max(res, square[0] * square[0])

print(res)
