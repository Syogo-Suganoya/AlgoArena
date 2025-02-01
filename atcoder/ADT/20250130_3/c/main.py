N = int(input())
H = list(map(int, input().split()))


def main():
    res_pos = 0

    for i in range(1, N):
        if H[res_pos] < H[i]:
            res_pos = i
        else:
            return H[res_pos]

    return H[res_pos]


print(main())
