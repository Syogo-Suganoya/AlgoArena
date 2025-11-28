N = int(input())
count = {}
pairs = set()

for _ in range(N - 1):
    A, B = map(int, input().split())
    count[A] = count.get(A, 0) + 1
    count[B] = count.get(B, 0) + 1
    pairs.add((A, B))

# まずペア数が N でない場合は即終了
if len(pairs) != N - 1:
    print("No")
    exit()

# N回登場する値があるかどうか
if any(v == N - 1 for v in count.values()):
    print("Yes")
else:
    print("No")
