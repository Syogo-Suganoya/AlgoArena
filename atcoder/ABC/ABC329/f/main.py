N, Q = map(int, input().split())

box = [set() for _ in range(N)]

C = list(map(int, input().split()))
for i in range(N):
    box[i].add(C[i])

for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    # small-to-large
    if len(box[a]) > len(box[b]):
        box[a], box[b] = box[b], box[a]

    for v in box[a]:
        box[b].add(v)

    box[a].clear()

    print(len(box[b]))
