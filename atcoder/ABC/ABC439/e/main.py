import bisect

N = int(input())
people = []

for _ in range(N):
    A, B = map(int, input().split())
    people.append((A, B))

# ① A を昇順
# ② A が同じなら B を降順
#    （同じ A の中で両方選ばれないようにするため）
people.sort(key=lambda x: (x[0], -x[1]))

# B だけ取り出す
B_list = [b for _, b in people]

# --------------------------
# LIS（最長増加部分列）を求める
# --------------------------
lis = []

for b in B_list:
    # lis の中で b を入れる位置を探す
    pos = bisect.bisect_left(lis, b)

    if pos == len(lis):
        # 末尾に追加できる場合
        lis.append(b)
    else:
        # 既存の値を更新
        lis[pos] = b

# lis の長さが答え
print(len(lis))
