N = int(input())
A = list(map(int, input().split()))

# 余りごとの個数をカウントするための辞書を用意
count = {}

# 各要素の 200 で割った余りを求めて、辞書にカウント
for a in A:
    mod = a % 200
    if mod not in count:
        count[mod] = 0
    count[mod] += 1

# 組み合わせの個数を数える
ans = 0
for mod in count:
    c = count[mod]
    if c >= 2:
        # c個の中から2つ選ぶ組み合わせ: cC2 = c * (c - 1) // 2
        ans += c * (c - 1) // 2

print(ans)
