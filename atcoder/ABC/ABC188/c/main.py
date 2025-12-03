n = int(input())
a = list(map(int, input().split()))

# 完全二分木のノード数は 2^(n+1) - 1
size = 1 << n
tree = [0] * (2 * size)

# 葉ノードに選手をセット
for i in range(size):
    tree[size + i] = i

# 下から順に勝者を木に記録
for i in range(size - 1, 0, -1):
    left = tree[2 * i]
    right = tree[2 * i + 1]
    if a[left] > a[right]:
        tree[i] = left
    else:
        tree[i] = right

# 準優勝は最後の勝者と戦った相手
winner = tree[1]
left = tree[2]
right = tree[3]
runner_up = right if left == winner else left

print(runner_up + 1)
