A, B, C, D = map(int, input().split())


# 素数判定
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 高橋くんが勝てるかどうかを判定
for a in range(A, B + 1):
    can_make_prime = False
    for c in range(C, D + 1):
        if is_prime(a + c):
            can_make_prime = True
            break  # あおきが素数を作れるのでこのaでは高橋くん負け
    if not can_make_prime:
        # このaではあおきが絶対素数を作れない → 高橋くんの勝ち確定
        print("Takahashi")
        break
else:
    # 全てのaにおいてあおきが素数作れる → 高橋くんの勝ち目なし
    print("Aoki")
