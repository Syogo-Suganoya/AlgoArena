import math

a, b = map(int, input().split())


# 落下までの時間を求める関数 f(n)
# n 回重力を強くした場合、落下時間は a / sqrt(n+1)、強化時間は b * n
def f(n):
    return a / math.sqrt(n + 1) + b * n


# 探索範囲の初期化
# 最悪でも a / b 回強化すれば f(n) は単調増加に転じると仮定して上限を設定
l, r = 0, a // b
# 三分探索：整数なので近づいたらforループで全探索に切り替える
while r - l > 2:
    m1 = (2 * l + r) // 3
    m2 = (l + 2 * r) // 3

    # 小さい方を探索範囲に残す
    if f(m1) > f(m2):
        l = m1
    else:
        r = m2

# 残った範囲での最小値を全探索で取得
ans = float("inf")
for i in range(l, r + 1):
    ans = min(ans, f(i))

print(f"{ans:.10f}")
