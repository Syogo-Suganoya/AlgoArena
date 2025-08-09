N, M = map(int, input().split())
A = list(map(int, input().split()))

total_votes = sum(A)
threshold = total_votes / (4 * M)  # 1/4以上かどうかの閾値

count = 0
for a in A:
    if a >= threshold:
        count += 1

if count >= M:
    print("Yes")
else:
    print("No")
