N = int(input())
records = []

for _ in range(N):
    S, T = input().split()
    T = int(T)
    records.append((T, S))

# T の降順でソート（大きい順）
records.sort(reverse=True)

# 2番目に大きい T の S を出力
print(records[1][1])
