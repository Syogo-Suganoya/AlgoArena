N = int(input())
A = list(map(int, input().split()))

res = N  # 長さ1の部分列（各要素）を数える
i = 0

while i < N - 1:
    j = i + 1
    # 2項目との差を計算
    di = A[j] - A[i]

    # jを動かして等差が保たれているか確認
    while j < N and A[j] - A[j - 1] == di:
        res += j - i  # 部分列の数を加算
        j += 1

    # i を j-2 まで飛ばして重複を避ける
    i = j - 2
    i += 1

print(res)
