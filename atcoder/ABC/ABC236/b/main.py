from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# カウント
count = Counter(A)

# ちょうど3回出現する値を出力
for num, c in count.items():
    if c == 3:
        print(num)
