N = int(input())
S = [input() for _ in range(N)]


def is_palindrome(s):
    return s == s[::-1]


for i in range(N):
    for j in range(N):
        if i != j:
            combined = S[i] + S[j]
            if is_palindrome(combined):
                print("Yes")
                exit()

print("No")
