N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]

# 締切（deadline）が早い順にソート
tasks.sort(key=lambda x: x[1])

# 経過時間（仕事を順にこなした合計時間）
current_time = 0

for duration, deadline in tasks:
    current_time += duration  # 現在の仕事をこなすのに必要な時間を加算
    if current_time > deadline:
        # 締切をオーバーしたらアウト
        print("No")
        exit()

# 全て締切に間に合った場合
print("Yes")
