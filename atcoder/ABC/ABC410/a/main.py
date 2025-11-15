N = int(input())
A = list(map(int, input().split()))
K = int(input())

# K以上の要素をカウント
count = sum(1 for a in A if a >= K)
print(count)
