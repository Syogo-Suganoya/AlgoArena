N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


def check(a, b):
    N = len(a)
    for i in range(N):
        for j in range(N):
            if a[i][j] == 1 and b[i][j] != 1:
                return False
    return True


def rotate_maze_clockwise(maze):
    """迷路を時計回りに90度回転"""
    return [list(row) for row in zip(*maze[::-1], strict=True)]


def main():
    a = A
    for _ in range(4):
        if check(a, B):
            return True
        a = rotate_maze_clockwise(a)
    return False


print("Yes" if main() else "No")
