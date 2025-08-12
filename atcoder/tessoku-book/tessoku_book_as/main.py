X = {x: i for i, x in enumerate("WBR")}  # 色を数字に変換

N, C = input().split()  # Nはカード枚数、Cは残したいカード色
C = X[C]  # 目標の色を数字に変換
A = input()  # カード列入力
A = [X[a] for a in A]  # 数字に変換

if sum(A) % 3 == C:
    print("Yes")
else:
    print("No")
