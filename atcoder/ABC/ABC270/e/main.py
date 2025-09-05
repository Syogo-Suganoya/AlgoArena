import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 優先度付きキュー（最小値をすぐ取り出せるようにする）
# (りんごの数, かごの番号) を格納
heap = [(a, i) for i, a in enumerate(A)]
heapq.heapify(heap)

# すでに引いた「周回数」を記録する
subtracted = 0

while heap:
    # 今最も小さいりんごの数を取り出す
    min_val, idx = heap[0]
    # そのかごに対して、まだ「min_val - subtracted」だけ残っている
    need = min_val - subtracted
    # 現在のかごの数
    count = len(heap)

    # もし「まとめて need 周」できるならやってしまう
    if K >= need * count:
        K -= need * count
        subtracted += need
        # 最小値のかごを削除（0 になった）
        while heap and heap[0][0] == min_val:
            heapq.heappop(heap)
    else:
        # まとめて消費できないなら、K // count 周だけまとめる
        rounds = K // count
        subtracted += rounds
        K -= rounds * count
        break

# ここまでで「まとめて処理できる分」は全部やった
# 残りの K は、まだあるかごから 1 個ずつシミュレーション
ans = [max(0, a - subtracted) for a in A]

i = 0
while K > 0:
    if ans[i] > 0:
        ans[i] -= 1
        K -= 1
    i += 1

print(*ans)
