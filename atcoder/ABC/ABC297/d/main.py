A, B = map(int, input().split())
ans = 0

while A != 0 and B != 0 and A != B:
    if A > B:
        # A から B を何回引けるかを足す
        ans += A // B
        A %= B
    else:
        ans += B // A
        B %= A

# A または B が 0 になってループを抜けた場合は、最後の1回が不要なので調整
if A == 0 or B == 0:
    ans -= 1  # 最後の加算分を引く（0 にしてしまった操作は無効とする）

print(ans)
