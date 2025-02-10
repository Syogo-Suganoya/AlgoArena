from itertools import combinations

# 入力
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]


def main():
    # H行の中からH2個を選ぶ, W列の中からW2個を選ぶ
    for row_indices in combinations(range(H), H2):
        for col_indices in combinations(range(W), W2):
            # # 部分行列を作成
            submatrix = [[A[i][j] for j in col_indices] for i in row_indices]
            # Bと一致するか判定
            if submatrix == B:
                return True
    return False


print("Yes" if main() else "No")
