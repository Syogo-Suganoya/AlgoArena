from collections import defaultdict

N, Q = map(int, input().split())
p = defaultdict(int)

for _ in range(Q):
    q, x = map(int, input().split())
    match q:
        case 1:
            p[x] += 1
        case 2:
            p[x] += 2
        case 3:
            print("Yes" if p[x] >= 2 else "No")
