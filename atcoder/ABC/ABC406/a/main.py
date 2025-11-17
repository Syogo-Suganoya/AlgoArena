from datetime import time

# 入力を整数で取得
A, B, C, D = map(int, input().split())

# timeオブジェクトを作成
t1 = time(hour=A, minute=B)
t2 = time(hour=C, minute=D)

# 比較
print("Yes" if t1 > t2 else "No")
