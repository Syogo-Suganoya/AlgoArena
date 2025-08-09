N = int(input())
A = list(map(int, input().split()))

# 順序を復元するためのリスト
order = [0] * N
for student_number, Ai in enumerate(A, start=1):
    order[Ai - 1] = student_number

print(*order)
