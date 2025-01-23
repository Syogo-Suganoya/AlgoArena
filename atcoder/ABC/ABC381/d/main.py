# 公式解説をpyに置換
# https://atcoder.jp/contests/abc381/editorial/11406

n = int(input())
a = list(map(int, input().split()))


def find_max_subsequence_length(n, a, start_index):
    last = [-2] * (200001)
    l = start_index
    ans = 0

    for i in range(start_index, n - 1, 2):
        if a[i] != a[i + 1]:
            l = i + 2
        else:
            l = max(l, last[a[i]] + 2)
        ans = max(ans, i + 2 - l)
        last[a[i]] = i

    return ans


def main():
    ans = find_max_subsequence_length(n, a, 0)
    ans = max(ans, find_max_subsequence_length(n, a, 1))

    print(ans)


if __name__ == "__main__":
    main()
