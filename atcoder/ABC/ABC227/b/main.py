def is_special_number(s):
    # 1 <= a, b <= 1000
    for a in range(1, 1001):
        for b in range(1, 1001):
            if 4 * a * b + 3 * a + 3 * b == s:
                return True  # 見つかったらすぐに True を返す
    return False  # 見つからなければ False を返す


N = int(input())
S = list(map(int, input().split()))

ans = 0
for s in S:
    if not is_special_number(s):
        ans += 1

print(ans)
