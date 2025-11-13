S = input()
T = set(input())

prev = ""
for c in S:
    if c.isupper():
        if prev != "" and prev not in T:
            print("No")
            break
    prev = c
else:
    print("Yes")
