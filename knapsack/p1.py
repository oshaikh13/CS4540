def solver(total_distance, clubs):
    dp = [None] * (total_distance + 1)
    dp[0] = 0 # base case
    for idx in range(1, total_distance + 1):
        for club in clubs:
            if idx - club >= 0 and dp[idx - club] is not None:
                dp[idx] = dp[idx - club] + 1 if dp[idx] is None else min(dp[idx], dp[idx - club] + 1)

    return dp[-1]

print(solver(100, [33, 66, 1]))

