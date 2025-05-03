def main():
    a, b, c, d, e, f = map(int, input().split())
    g, h, i, j, k, l = map(int, input().split())

    x1 = (a, d)
    y1 = (b, e)
    z1 = (c, f)

    x2 = (g, j)
    y2 = (h, k)
    z2 = (i, l)

    left_x = max(x1[0], x2[0])
    right_x = min(x1[1], x2[1])

    overlap_x = left_x < right_x

    left_y = max(y1[0], y2[0])
    right_y = min(y1[1], y2[1])

    overlap_y = left_y < right_y

    left_z = max(z1[0], z2[0])
    right_z = min(z1[1], z2[1])

    overlap_z = left_z < right_z

    return overlap_x and overlap_y and overlap_z


print("Yes" if main() else "No")
