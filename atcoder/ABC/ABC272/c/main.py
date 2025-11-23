# 入力
N = int(input())
A = list(map(int, input().split()))

even = []
odd = []

# 偶数と奇数に分ける
for x in A:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

# 大きい順に並び替え
even.sort(reverse=True)
odd.sort(reverse=True)

candidates = []

# 偶数同士で作れる？
if len(even) >= 2:
    candidates.append(even[0] + even[1])

# 奇数同士で作れる？
if len(odd) >= 2:
    candidates.append(odd[0] + odd[1])

# 結果の出力
if candidates:
    print(max(candidates))
else:
    print(-1)
