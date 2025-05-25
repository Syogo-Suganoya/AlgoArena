N = int(input())
A = list(map(int, input().split()))

prev = A[0]
count = 1
found = False

for i in range(1, N):
    if A[i] == prev:
        count += 1
        if count >= 3:
            # 3以上の連続する要素が見つかったらフラグを立てて終了
            found = True
            break
    else:
        # 連続しない場合はカウントリセット
        prev = A[i]
        count = 1

print("Yes" if found else "No")
