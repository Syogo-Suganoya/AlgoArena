from collections import Counter

# 入力の受け取り
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Aの要素数を数える（重複を管理するため）
count_A = Counter(A)

# Bの各要素をチェック
for b in B:
    # Aにbが存在しない、または在庫がないならNG
    if count_A[b] == 0:
        print("No")
        break
    # Aから1個使う
    count_A[b] -= 1
else:
    # 全てOKならYes
    print("Yes")
