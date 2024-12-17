N, c1, c2 = map(str, input().split())
S = input()

N = int(N)


def find_all_indices(string, char):
    return [i for i, c in enumerate(string) if c == char]


a = find_all_indices(S, c1)
res = c2 * N
res = list(res)
for i in range(N):
    if i in a:
        res[i] = c1

print("".join(res))
