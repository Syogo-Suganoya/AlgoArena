N = int(input())
A = list(map(int, input().split()))

# 番号 → 世代 を管理
# 最初のアメーバは番号 1 で世代 0
gen = {1: 0}
max_no = 1  # 現在の最大番号

for x in A:
    t = gen[x]  # 選ばれたアメーバの世代
    # 新しいアメーバ 2 匹を追加
    for _ in range(2):
        max_no += 1
        gen[max_no] = t + 1

# 出力: 番号順に世代を出す
for i in range(1, max_no + 1):
    print(gen[i])
