N, M = map(int, input().split())

count = 0
for i in range(N, M + 1):
    str_i = str(i)
    if str_i == str_i[::-1]:
        count += 1
print(count)
