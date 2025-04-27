N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

count = defaultdict(int)

ans = N + 1
left = 0

# 尺取り法
for right in range(N):
    # まず右を決め、その値のカウントを+1する
    count[A[right]] += 1

    # 値が2回登場するまで、右を進める
    # その範囲で値が複数回登場するまで、左を進める
    while count[A[right]] >= 2:
        ans = min(ans, right - left + 1)

        # 重複した値のカウントを-1する
        count[A[left]] -= 1
        # 左を進める
        left += 1

print(ans if ans != N + 1 else -1)


def another():
    """別解"""
    # 解の初期値はNより長く
    ans = N + 1

    # 値とインデックス数を二次元リストで管理。[値][インデックス]
    pos = [[] for _ in range(1_000_001)]
    for i in range(N):
        pos[A[i]].append(i)

    # posをループ
    for i in range(len(pos)):
        # 複数回登場しない値はスキップ
        if len(pos[i]) <= 1:
            continue
        # インデックスを取得し、ansを更新する
        for j in range(len(pos[i]) - 1):
            cur = pos[i][j + 1] - pos[i][j] + 1
            ans = min(ans, cur)

    if ans == N + 1:
        print(-1)
    else:
        print(ans)
