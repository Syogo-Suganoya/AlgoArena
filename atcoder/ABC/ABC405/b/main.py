n, m = map(int, input().split())
a = list(map(int, input().split()))

# 0-indexed にそろえる
for i in range(n):
    a[i] -= 1


def has_missing_value(arr, m):
    """
    arr の中に 0..m-1 がすべて含まれているかをチェックする関数。
    ・含まれていない値があれば True（= 抜けがある）
    ・すべて揃っていれば False
    """
    exist = [False] * m
    for x in arr:
        exist[x] = True
    for v in exist:
        if not v:
            return True
    return False


ans = 0

while True:
    # 抜け番が発生したら終了
    if has_missing_value(a, m):
        break

    # なければ末尾を削って次
    ans += 1
    a.pop()

print(ans)
