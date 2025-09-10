N = int(input())  # 入力を整数として受け取る
count = 0  # 条件を満たす数のカウント

# 前半の数字を生成
for i in range(1, 1000001):  # 1 から 1000000 までの数字を試す
    doubled = int(str(i) + str(i))  # 前半と後半を繰り返す
    if doubled <= N:  # N 以下であればカウント
        count += 1
    else:
        break  # それ以上の数は N を超えるので終了

print(count)  # 結果を出力
