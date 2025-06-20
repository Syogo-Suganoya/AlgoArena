N = int(input())
A = list(map(int, input().split()))

# 呼ばれたかどうかを記録するリスト（1～Nを使うので長さ N+1）
called = [False] * (N + 1)

# i を 1～N の順で見ていく
for i in range(1, N + 1):
    if not called[i]:  # まだ呼ばれていなければ
        called[A[i - 1]] = True  # A[i] の人を「呼ばれた」とする

# 呼ばれていない人の番号を集める
result = [i for i in range(1, N + 1) if not called[i]]

print(len(result))
print(*result)
