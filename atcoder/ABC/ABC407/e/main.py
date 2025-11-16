import heapq


def solve():
    n = int(input())
    a = []
    for _ in range(2 * n):
        a.append(int(input()))

    ans = 0
    # Pythonのリストをヒープとして使用
    que = []

    for i in range(n):
        if i == 0:
            # i=0 の場合: a[0*2 - 0] -> a[0] を push
            heapq.heappush(que, -a[0])
        else:
            # i > 0 の場合:
            # a[i*2 - 1] -> a[2*i - 1] を push
            # a[i*2 - 0] -> a[2*i] を push
            heapq.heappush(que, -a[2 * i - 1])
            heapq.heappush(que, -a[2 * i])

        # ヒープから最大値を取り出す
        # (最小の負の数を取り出し、正に戻す)
        v = -heapq.heappop(que)

        # 答えに加算
        ans += v

    return ans


T = int(input())

for _ in range(T):
    print(solve())
