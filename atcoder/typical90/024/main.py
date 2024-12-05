N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def main():
    # Step #2: 差分の計算
    Diff = 0
    for i in range(N):
        Diff += abs(A[i] - B[i])

    # Step #3: 差分がKを超えている場合
    if Diff > K:
        print("No")
        return

    # Step #4: 偶奇の確認
    if Diff % 2 != K % 2:
        print("No")
        return

    # Step #5: 出力
    print("Yes")


main()
