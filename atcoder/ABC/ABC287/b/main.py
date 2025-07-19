N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

T = set(T)
count = 0

for s in S:
    if s[-3:] in T:  # 末尾3文字がTに含まれているか
        count += 1

print(count)
