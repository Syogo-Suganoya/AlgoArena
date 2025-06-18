N, M, T = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]


def main():
    now = N  # 現在のバッテリー量（最初は満タン）
    last = 0  # 前回の時刻（出発時刻）

    for a, b in AB:
        # aまでに減る分
        now -= a - last
        if now <= 0:
            return False

        # カフェでの回復分（上限あり）
        now += b - a
        if now > N:
            now = N

        last = b  # 最終時刻を更新

    # 最後（last → t）までの減少
    now -= T - last
    return now > 0


print("Yes" if main() else "No")
