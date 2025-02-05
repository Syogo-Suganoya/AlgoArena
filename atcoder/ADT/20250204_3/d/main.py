H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]


def is_shifted_match(s, t):
    """A を s 回縦シフトし、t 回横シフトしたとき B と一致するか判定"""
    for i in range(H):
        for j in range(W):
            if A[(i + s) % H][(j + t) % W] != B[i][j]:
                return False
    return True


def main():
    for s in range(H):
        for t in range(W):
            if is_shifted_match(s, t):
                return True
    return False


print("Yes" if main() else "No")
