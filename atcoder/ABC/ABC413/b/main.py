N = int(input())
S_list = [input() for _ in range(N)]

s = set()

# N個の文字列から2つ選ぶ全探索
for i in range(N):
    for j in range(N):
        if i == j:
            continue  #
        t = S_list[i] + S_list[j]
        s.add(t)

print(len(s))
