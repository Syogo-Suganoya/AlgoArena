N = int(input())
A = list(map(int, input().split()))

used = set()
for x in A:
    if x != -1:
        if x in used:
            print("No")
            exit()
        used.add(x)

# 出てこない数字を管理
unused = [i for i in range(1, N + 1) if i not in used]
unused_idx = 0

res = []
for x in A:
    if x == -1:
        res.append(unused[unused_idx])
        unused_idx += 1
    else:
        res.append(x)

print("Yes")
print(*res)
