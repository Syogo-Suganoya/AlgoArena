N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    ones = []
    for i in range(len(A)):
        if A[i] == 1:
            ones.append(str(i + 1))  # 1-indexed にするために +1
    print(" ".join(ones))
