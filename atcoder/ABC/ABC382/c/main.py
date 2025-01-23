N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

K = 200001
id_list = [-1] * K
r = K

for i in range(N):
    a = A[i]
    while r > a:
        r -= 1
        id_list[r] = i + 1

result = [id_list[b] for b in B]

print('\n'.join(map(str, result)))
