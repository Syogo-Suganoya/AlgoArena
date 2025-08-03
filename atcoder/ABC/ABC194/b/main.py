N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

res = float("inf")

for i in range(N):
    for j in range(N):
        if i == j:
            # 同じ人が両方やる場合（直列）
            res = min(res, A[i] + B[i])
        else:
            # 別の人が並列でやる場合（遅い方に合わせる）
            res = min(res, max(A[i], B[j]))

print(res)


def ano():
    """O(N) solution"""

    # 入力
    N = int(input())
    A, B = [], []

    # A: 最初に依頼する場合の時間、B: 次に依頼する場合の時間
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # Aの最小値のインデックス（最も早く仕事を終えられる人）
    i = A.index(min(A))
    # Bの最小値のインデックス（次の仕事を最も早く終えられる人）
    j = B.index(min(B))

    # 最も早いAと最も早いBが同じ人の場合
    if i == j:
        a, b = A[i], B[i]
        # 同じ人に両方任せる場合の時間：a + b

        # 他の候補と比較するため、一時的にその人を削除
        del A[i]
        del B[i]

        # 3通りの比較：
        # 1. 同じ人に両方任せる（a + b）
        # 2. a（最速のA）と別のBの最小値（ただし同一人物除外）
        # 3. b（最速のB）と別のAの最小値
        ans = min(
            a + b,  # 同じ人に両方任せる
            max(min(A), b),  # 最速のBの人にBを、別の最速Aの人にAを任せる
            max(a, min(B)),  # 最速のAの人にAを、別の最速Bの人にBを任せる
        )

    # 最速のAと最速のBが別の人なら、同時進行可能
    else:
        ans = max(A[i], B[j])  # 並列実行なので、遅い方の時間がかかる

        # 最小時間を出力
        print(ans)
