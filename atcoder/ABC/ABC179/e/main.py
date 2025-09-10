n, x, m = map(int, input().split())

# 「この数が現れたのは何番目か」を記録するリスト
seen = [-1] * m

a_seq = []
total = 0
idx = 0
while seen[x] == -1:
    seen[x] = idx
    a_seq.append(x)  # 数列に追加
    total += x  # 合計に追加
    idx += 1
    x = (x * x) % m  # 次の A_n を計算

start = seen[x]  # ループ開始の index
length = idx - start  # ループの長さ
loop_sum = sum(a_seq[start:])  # ループの総和

# N 項の合計を計算
ans = 0
if n <= idx:
    ans = sum(a_seq[:n])
else:
    ans += total
    n -= idx
    ans += (n // length) * loop_sum
    n %= length
    ans += sum(a_seq[start : start + n])

print(ans)
