N, M = map(int, input().split())
S = [input() for _ in range(N)]
target = [
    "###.?????",
    "###.?????",
    "###.?????",
    "....?????",
    "?????????",
    "?????....",
    "?????.###",
    "?????.###",
    "?????.###",
]
n, m = len(target), len(target[0])


# (y, x) を左上とする 9×9 の領域が条件を満たすか判定する関数
def matches_pattern(y, x):
    for dy in range(n):
        for dx in range(m):
            current_char = S[y + dy][x + dx]
            target_char = target[dy][dx]

            # `#` や `.` は完全一致する必要がある
            if target_char in "#." and current_char != target_char:
                return False  # 1つでも条件を満たさないなら False

    return True  # すべて条件を満たしたら True


# 9×9 のパターンが一致する開始位置を探す
for y in range(N - n + 1):
    for x in range(M - m + 1):
        if matches_pattern(y, x):
            print(y + 1, x + 1)  # 1-indexed で出力
