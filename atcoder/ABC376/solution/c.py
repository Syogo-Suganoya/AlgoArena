# 公式解説をpyに置換
# https://atcoder.jp/contests/abc376/editorial/11193

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    for i in range(n - 1):
        if a[i] > b[i]:
            print(-1)
            return

    for i in range(n - 2, -1, -1):
        if a[i + 1] > b[i]:
            print(a[i + 1])
            return

    print(a[0])


if __name__ == "__main__":
    main()
