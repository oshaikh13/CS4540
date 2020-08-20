items = [(3, 30), (4, 50), (5, 60)]
total_val = sum(v[1] for v in items)
capacity = 8

def solver(n, v, capacity):

    dp = [[float('inf') for i in range(v + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        weight, val = items[i - 1]
        for j in range(1, v + 1):
            dp[i][j] = min(dp[i - 1][j - val] + weight, dp[i - 1][j]) if val - j <= 0 else dp[i - 1][j]

    res = 0
    for idx, elem in enumerate(dp[-1]):
        if elem <= capacity:
            res = idx

    return res

print(solver(len(items), total_val, capacity))
