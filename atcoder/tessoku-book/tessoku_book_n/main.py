N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))


def main():
    # 箱 A と B の組み合わせの合計をリスト P に格納
    P = [a + b for a in A for b in B]

    # 箱 C と D の組み合わせの合計をリスト Q に格納
    Q = [c + d for c in C for d in D]

    # Q をセットに変換して高速に検索できるようにする
    Q_set = set(Q)

    # P の各要素について、K - P_i が Q に含まれているかを確認
    for p in P:
        if K - p in Q_set:
            return True

    return False


print("Yes" if main() else "No")
