A, B, C, X = map(int, input().split())

if X <= A:
    print(1)  # A以下なら100%
elif X > B:
    print(0)  # Bより大きければ確率は0%
else:
    print(C / (B - A))  # 区間 (A, B] の間なら一様分布として C / (B-A)
