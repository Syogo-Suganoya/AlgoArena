# 公式解説をpyに置換
# https://atcoder.jp/contests/abc381/editorial/11413

N = int(input())
S = input()


def main():
    ans = 0
    for i in range(N):
        if S[i] != '/':
            continue
        d = 0
        while True:
            j = i - (d + 1)
            k = i + (d + 1)
            if not (0 <= j < N):
                break
            if not (0 <= k < N):
                break
            if S[j] != '1':
                break
            if S[k] != '2':
                break
            d += 1
        ans = max(ans, 1 + d * 2)

    print(ans)


if __name__ == "__main__":
    main()
