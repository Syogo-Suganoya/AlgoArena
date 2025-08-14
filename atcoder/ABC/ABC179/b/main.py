N = int(input())
count = 0

for _ in range(N):
    A, B = map(int, input().split())
    if A == B:
        count += 1  # ゾロ目ならカウントを1増やす
        if count == 3:
            print("Yes")
            exit()  # 見つけたら即終了
    else:
        count = 0  # ゾロ目じゃないのでリセット

print("No")  # 最後まで3連続ゾロ目がなかった場合
