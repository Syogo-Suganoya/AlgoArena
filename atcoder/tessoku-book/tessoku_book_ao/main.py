n = int(input())
s = input()
for i in range(n - 2):
    if s[i : i + 3] == "RRR" or s[i : i + 3] == "BBB":
        print("Yes")
        exit()
print("No")
