N = int(input())

x = [0]
id = 0

result = []
for _ in range(N):
    q = input().split()
    match q[0]:
        case "1":
            l = int(q[1])
            x.append(x[-1] + l)
        case "2":
            id += 1
        case "3":
            k = int(q[1]) - 1
            print(x[id + k] - x[id])
