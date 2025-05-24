N = int(input())

logged = False
res = 0
for i in range(N):
    S = input()
    match S:
        case "login":
            logged = True
        case "logout":
            logged = False
        case "public":
            pass
        case "private":
            if not logged:
                res += 1
print(res)
