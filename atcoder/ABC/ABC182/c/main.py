N = input()

digits = list(map(int, N))  # 各桁を数字に分解
mod3 = [d % 3 for d in digits]
digit_sum = sum(digits)
rem = digit_sum % 3  # 桁和の mod3

if rem == 0:
    print(0)  # そのままで3の倍数
elif rem == 1:
    # rem=1 → 1を1個消す or 2を2個消す
    if 1 in mod3 and len(digits) > 1:
        print(1)
    elif mod3.count(2) >= 2 and len(digits) > 2:
        print(2)
    else:
        print(-1)
elif rem == 2:
    # rem=2 → 2を1個消す or 1を2個消す
    if 2 in mod3 and len(digits) > 1:
        print(1)
    elif mod3.count(1) >= 2 and len(digits) > 2:
        print(2)
    else:
        print(-1)
