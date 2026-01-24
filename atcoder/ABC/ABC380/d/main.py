# 公式解説をpyに置換
# https://atcoder.jp/contests/abc380/editorial/11362


def popcount(n):
    # nの二進数表現で1の個数をカウントする
    return bin(n).count("1")


# メイン処理
def main():
    s = input()  # 入力文字列
    q = int(input())  # クエリ数
    queries = list(map(int, input().split()))  # クエリをリストとして取得

    result = []
    for i in range(q):
        k = queries[i] - 1  # 0-index化
        blk = k // len(s)  # ブロック番号
        pt = k % len(s)  # ブロック内のインデックス
        if popcount(blk) % 2:  # blkの1の個数が奇数なら反転
            result.append(s[pt].swapcase())
        else:  # そのまま
            result.append(s[pt])

    print(" ".join(result))


main()
