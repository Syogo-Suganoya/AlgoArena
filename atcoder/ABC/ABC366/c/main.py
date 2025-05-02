from collections import defaultdict

Q = int(input())

d = defaultdict(int)  # 種類のカウント
kinds = set()  # 現在存在する種類の集合（カウントが1以上）

for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            x = query[1]
            d[x] += 1
            kinds.add(x)  # xのカウントが1以上であることを集合で管理
        case 2:
            x = query[1]
            if d[x] > 0:
                d[x] -= 1
                if d[x] == 0:
                    kinds.discard(x)  # 種類が0になったら集合から削除
        case 3:
            print(len(kinds))  # 現在の種類数を出力
