def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


N = int(input())
max_root = int(N ** (1 / 3)) + 1  # 立方根の上限を計算

for i in range(max_root, 0, -1):
    cube = i**3
    if cube <= N and is_palindrome(cube):
        print(cube)
        break
