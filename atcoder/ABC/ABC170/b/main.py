N, M = map(int, input().split())


def main():
    # 亀の数を計算
    kame = (M - 2 * N) // 2
    tsuru = N - kame

    # 条件を満たすか確認
    return kame >= 0 and tsuru >= 0 and 2 * tsuru + 4 * kame == M


print("Yes" if main() else "No")
