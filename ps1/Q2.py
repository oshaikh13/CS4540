# PLEASE USE PYPY3 TO RUN ON DMOJ, NOT PYTHON

import sys
all_data = sys.stdin.read().split('\n')[:-1]
capacity = int(all_data[0].split(" ")[-1])

items = []
total_val = 0

for row in all_data[1:]:
    items.append([int(x) for x in row.split(" ")])
    total_val += items[-1][-1]

def solver(n, v, capacity):

    dp = [[float('inf') for i in range(v + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        weight, val = items[i - 1]
        for j in range(1, v + 1):
            dp[i][j] = min(dp[i - 1][j - val] + weight, dp[i - 1][j]) if val - j <= 0 else dp[i - 1][j]

    sol = 0
    for idx, elem in enumerate(dp[-1]):
        if elem <= capacity:
            sol = idx

    return sol

print(solver(len(items), total_val, capacity))
