N = int(input())
P = list(map(int, input().split()))

cnt = [0] * N

# 回転sで満足できる人の数を集計
for i in range(N):
    shift = (i - P[i]) % N
    cnt[shift] += 1

# 尺取り法（±1の3連続区間の合計最大を取る）
cnt += cnt[:2]  # 円形なので前後をつなぐ
max_val = 0
for i in range(N):
    max_val = max(max_val, cnt[i] + cnt[i + 1] + cnt[i + 2])

print(max_val)
