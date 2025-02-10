import heapq

N = int(input())  # 入力の個数
A = []
for i in range(N):
    s, c = map(int, input().split())  # (整数 s, その個数 c) を受け取る
    heapq.heappush(A, (s, c))  # (s, c) をヒープに格納


ans = 0  # 最終的に残る整数の個数
while A:
    s, c = heapq.heappop(A)  # 最小の (s, c) を取り出す
    while A and s == A[0][0]:  # 同じ s をまとめる
        ss, cc = heapq.heappop(A)
        c += cc  # 個数を合算
    ans += c % 2  # 合成後に1つ余ったら、カウントする
    if c >= 2:  # 2個以上ある場合、次の整数 s*2 を作る
        heapq.heappush(A, (s * 2, c // 2))  # (s*2, c//2) を追加
print(ans)
