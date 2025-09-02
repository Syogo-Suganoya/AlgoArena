N, T, M = map(int, input().split())
bad_pairs = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    bad_pairs[a].add(b)
    bad_pairs[b].add(a)

ans = 0


def dfs(player, teams):
    """
    player: 現在割り当てる選手の番号
    teams: list of sets, 各チームにいる選手の集合
    """
    global ans
    if player == N:
        # 全員割り当て終わり
        if len(teams) == T:
            ans += 1
        return

    # 既存のチームに入れる場合
    for i, team in enumerate(teams):
        # 相性の悪い人がいないか確認
        if any(p in bad_pairs[player] for p in team):
            continue
        team.add(player)
        dfs(player + 1, teams)
        team.remove(player)

    # 新しいチームを作って入れる場合
    if len(teams) < T:
        teams.append({player})
        dfs(player + 1, teams)
        teams.pop()


# 最初は誰も割り当てていない
dfs(0, [])

print(ans)
