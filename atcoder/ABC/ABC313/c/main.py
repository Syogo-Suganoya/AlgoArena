N = int(input())
A = list(map(int, input().split()))

# Aの総和を計算
sum_a = sum(A)

# 総和をNで割ったときの余りを記録（＝割り切れない分の要素が1多くなる）
m = sum_a % N

# 各要素が floor(sum_a / N) になるように基準リストを作成
avg = sum_a // N
B = [avg] * N

# 余りの分だけ、大きい値（avg + 1）を1つずつ後ろから与えて調整
for i in range(m):
    B[N - 1 - i] += 1

# ソートしてから差を取ることで、最小の移動量になる
A.sort()

# AとBの要素の差の合計を取る
res = 0
for a, b in zip(A, B, strict=True):
    res += abs(a - b)

# 各移動は一対一対応で2倍カウントされているので、最後に2で割る
print(res // 2)
