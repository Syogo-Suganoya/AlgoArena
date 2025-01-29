N = int(input())
A = list(map(int, input().split()))
P = 0
field = [0, 0, 0, 0]  # マスの状態を管理する list

for x in A:
    next_field = [0, 0, 0, 0]  # 次のマスの状態を管理する list
    field[0] = 1  # マス 0 にコマを置く
    for i in range(4):
        if field[i] == 1:
            if i + x >= 4:  # i + x >= 4 かどうかに応じて場合分け
                P += 1
            else:
                next_field[i + x] = 1
    field = next_field

print(P)
