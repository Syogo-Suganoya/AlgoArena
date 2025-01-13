def main():
    n = int(input())
    a = list(map(int, input().split()))

    cumulative_stone_transfer = [0] * n  # 累積での石の移動を管理
    transfer_diff = [0] * (n + 1)  # いもす法による差分管理

    for i in range(n):
        # 累積石移動の更新
        if i != 0:
            cumulative_stone_transfer[i] = (
                cumulative_stone_transfer[i - 1] + transfer_diff[i]
            )
            a[i] += cumulative_stone_transfer[i]

        # 次に渡す石の数を計算
        transferable_stones = min(n - i - 1, a[i])
        a[i] -= transferable_stones

        # いもす法の差分更新
        transfer_diff[i + 1] += 1
        transfer_diff[min(n, i + transferable_stones + 1)] -= 1

    # 結果の出力
    print(" ".join(map(str, a)))


if __name__ == "__main__":
    main()
