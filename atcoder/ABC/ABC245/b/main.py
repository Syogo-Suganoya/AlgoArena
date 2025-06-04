N = int(input())
A = list(map(int, input().split()))

A_set = set(A)

# 0からNのいずれかが必ず1つ欠けている前提
# 0からNまでをループして、存在しない数字を探す
for i in range(N + 1):
    if i not in A_set:
        print(i)  # 見つかったら出力して終了
        exit()
