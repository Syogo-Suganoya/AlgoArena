N = int(input().rstrip())
T = input().rstrip()

# 0 の出現数の累積を取る（prefix 0-count）
# A[i] = T[0..i-1] 中の '0' の個数
A = [0] * (N + 1)
for i in range(N):
    A[i + 1] = A[i] + (1 if T[i] == "0" else 0)

# 偶数個の 0 までの位置カウント、奇数個の 0 までの位置カウント
even_count = 0
odd_count = 0

for k in range(N + 1):
    if A[k] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# 部分文字列の 0 の数 = A[j]-A[i]
# これが偶数になる ↔ A[i] と A[j] が同じパリティ
# よって
# A[i],A[j] 両方偶数 → even_countC2 個
even_pairs = even_count * (even_count - 1) // 2

# A[i],A[j] 両方奇数 → odd_countC2 個
odd_pairs = odd_count * (odd_count - 1) // 2

# 全体の組み合わせ数
result = even_pairs + odd_pairs

print(result)
