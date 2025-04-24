N, Q = map(int, input().split())
nest = [1] * N
pigeons = list(range(1, N + 1))

res = 0

for i in range(Q):
    query = input()
    type_number = int(query[0])
    match type_number:
        case 1:
            query = query.split()
            P, H = int(query[1]), int(query[2])

            # 移動前の巣の元の数が2なら減算
            if nest[pigeons[P - 1] - 1] == 2:
                res -= 1
            # 移動先の巣の元の数が1なら加算
            if nest[H - 1] == 1:
                res += 1

            # 移動前の巣
            nest[pigeons[P - 1] - 1] -= 1
            # 移動先の巣
            nest[H - 1] += 1
            # 鳩の巣を移動
            pigeons[P - 1] = H
        case 2:
            print(res)
