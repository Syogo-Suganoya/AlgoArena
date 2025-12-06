N = int(input())
H = list(map(int, input().split()))

# 右から左へ調整
for i in range(N - 2, -1, -1):
    # H[i] が H[i+1] よりも 2 以上高ければ無理
    if H[i] > H[i + 1] + 1:
        print("No")
        break
    # 高さが 1 高ければ 1 低くする
    if H[i] == H[i + 1] + 1:
        H[i] -= 1
else:
    # break されずに最後までいけたなら成功
    print("Yes")
