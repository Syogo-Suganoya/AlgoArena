N = int(input())
S = input().strip()


def main():
    # 1 の位置をリスト A に記録
    A = [i for i in range(N) if S[i] == "1"]
    M = len(A)

    # 中央値を基準に移動回数を計算
    median = A[M // 2]

    ans = 0
    # 左端の位置
    left = median - (M // 2)
    for i in range(M):
        # A[i] は i番目の「1」がある位置
        now_position = A[i]

        # 「中央値」からM//2だけ左にずらした位置から順番に詰めていく
        target_position = left + i

        # そのために必要な移動量（距離）を計算
        move_cost = abs(now_position - target_position)

        # 答えに加算する
        ans += move_cost

    print(ans)


if __name__ == "__main__":
    main()
