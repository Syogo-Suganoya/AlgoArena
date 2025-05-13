N, Q = map(int, input().split())
S = input()
s = 0
for i in range(Q):
    t, x = map(int, input().split())
    match t:
        case 1:
            s = (s - x) % N
        case 2:
            print(S[(s + x - 1) % N])
