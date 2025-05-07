import heapq

# スライムの数 N を受け取り、各スライム (サイズ, 個数) をリストとして取得
N = int(input())
Q = [tuple(map(int, input().split())) for _ in range(N)]

# サイズの小さい順に処理するため、優先度付きキュー（ヒープ）に変換
heapq.heapify(Q)

ans = 0  # 最終的に残るスライムの個数

while len(Q):
    s, c = heapq.heappop(Q)  # 最も小さいサイズのスライムを取り出す

    # 同じサイズのスライムが他にもあれば、個数をまとめる
    while len(Q) and Q[0][0] == s:
        ss, cc = heapq.heappop(Q)
        c += cc

    ans += c % 2  # 奇数個あれば1体だけ残る（偶数個ならすべて合成可能）

    # 2個ずつ合成してサイズを2倍にしたスライムを次の処理対象としてヒープに追加
    if c > 1:
        heapq.heappush(Q, (s * 2, c // 2))

# 残ったスライムの合計を出力
print(ans)
