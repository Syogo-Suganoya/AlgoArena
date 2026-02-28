S = input()

count_a = 0
count_ab = 0
ans = 0

for ch in S:
    match ch:
        case "A":
            count_a += 1
        case "B":
            if count_a > 0:
                count_a -= 1
                count_ab += 1
        case "C":
            if count_ab > 0:
                count_ab -= 1
                ans += 1

print(ans)
