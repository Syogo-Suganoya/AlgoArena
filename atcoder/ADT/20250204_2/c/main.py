N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


def rotate_maze_clockwise(maze):
    """迷路を時計回りに90度回転"""
    return [list(row) for row in zip(*maze[::-1], strict=True)]


def check(A, B):
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                continue
            if B[i][j] == 0:
                return False
    return True


def main(A, B):
    for _ in range(4):
        A = rotate_maze_clockwise(A)
        if check(A, B):
            return True
    return False


print("Yes" if main(A, B) else "No")
