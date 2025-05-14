S = list(input().split())
T = list(input().split())


def main():
    co = 0
    # 元々あっている個数
    for i in range(3):
        if S[i] == T[i]:
            co += 1
    # 1つのみ正しい場合、1回の操作で正しい位置になる
    # その後は、正しい位置に戻すためには奇数回で終わってしまう
    return co != 1


print("Yes" if main() else "No")
