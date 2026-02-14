N = int(input())
A = list(map(int, input().split()))

MAX_DIGIT = max(A) + 5  # 必要な桁数

imos = [0] * (MAX_DIGIT + 1)

# 各 Ai について「0 〜 Ai-1 桁目」に +1
for a in A:
    imos[0] += 1
    imos[a] -= 1

# 累積和で各桁の値を作る
for i in range(1, MAX_DIGIT + 1):
    imos[i] += imos[i - 1]

# 繰り上げ処理
for i in range(MAX_DIGIT):
    carry = imos[i] // 10
    imos[i] %= 10
    imos[i + 1] += carry

# 上位ゼロ削除
idx = MAX_DIGIT
while idx > 0 and imos[idx] == 0:
    idx -= 1

# 出力（上位から）
print("".join(map(str, imos[idx::-1])))
