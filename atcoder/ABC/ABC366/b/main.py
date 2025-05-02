N = int(input())
lines = [input() for _ in range(N)]
max_len = max(len(line) for line in lines)

for i in range(max_len):
    row = ""
    for line in reversed(lines):
        row += line[i] if i < len(line) else "*"
    print(row.rstrip("*"))  # 最後の * を省く
