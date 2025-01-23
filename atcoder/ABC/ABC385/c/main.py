def max_illuminated_buildings():
    max_count = 0

    # 各 K を試す
    for K in range(1, N + 1):
        # 各開始点 start を試す
        for start in range(N - K + 1):
            current_count = 0
            current_height = H[start]
            # start, start+K, start+2K, ... の位置を探索
            for i in range(start, N, K):
                if H[i] != current_height:
                    break
                current_count += 1
            max_count = max(max_count, current_count)
    return max_count


N = int(input())
H = list(map(int, input().split()))
print(max_illuminated_buildings())
