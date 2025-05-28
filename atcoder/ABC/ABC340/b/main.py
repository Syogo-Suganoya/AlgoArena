N = int(input())
l = []
for i in range(N):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            l.append(query[1])
        case 2:
            print(l[-(query[1])])
