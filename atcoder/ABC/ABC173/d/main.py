N = int(input())
A = list(map(int, input().split()))

# 降順にソートして好意度の高い人から順に並べる
A.sort(reverse=True)

# 最初の人は最も好意度が高い人なので、まずその分を加える
ans = A[0]

# 2人ずつで1人を支える構造 → i//2 + 1 で親を指定
for i in range(N - 2):
    ans += A[i // 2 + 1]

print(ans)
