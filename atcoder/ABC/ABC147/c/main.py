N = int(input())

# honest[i]: i番目の人が「正直者」と言った人のインデックスリスト
# liar[i]: i番目の人が「不親切者」と言った人のインデックスリスト
honest = [[] for _ in range(N)]
liar = [[] for _ in range(N)]

# 各人の証言を受け取る
for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        # y==1なら正直者と言っている
        if y == 1:
            honest[i].append(x - 1)
        else:
            # y==0なら不親切者と言っている
            liar[i].append(x - 1)

max_honest = 0  # 最大の正直者数を記録

# 全ての「正直者・不親切者」パターンをビット全探索
for mask in range(1 << N):
    valid = True  # 証言の矛盾がないかのフラグ
    count = 0  # このパターンでの正直者数

    for i in range(N):
        # i番目の人が正直者なら (maskのiビットが1)
        if (mask >> i) & 1:
            count += 1
            # iが正直者なら、その証言は真実でなければならない
            # 正直者リストの人は正直者でなければならない
            for h in honest[i]:
                if not ((mask >> h) & 1):
                    valid = False  # 矛盾発見
                    break
            # 不親切者リストの人は正直者であってはいけない
            for l in liar[i]:
                if (mask >> l) & 1:
                    valid = False  # 矛盾発見
                    break
        if not valid:
            break  # 矛盾があれば、もうこのパターンは無効なので早めに抜ける

    if valid:
        # 矛盾がなければ最大値を更新
        max_honest = max(max_honest, count)

print(max_honest)
