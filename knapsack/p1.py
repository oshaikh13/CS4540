import sys
all_data = [int(x) for x in sys.stdin.read().split('\n')[:-1]]

def solver(total_distance, clubs):
    dp = [None] * (total_distance + 1)
    dp[0] = 0 # base case
    for idx in range(1, total_distance + 1):
        for club in clubs:
            if idx - club >= 0 and dp[idx - club] is not None:
                dp[idx] = dp[idx - club] + 1 if dp[idx] is None else min(dp[idx], dp[idx - club] + 1)

    return dp[-1]

res = solver(all_data[0], all_data[2:])
if res is not None:
    print("Roberta wins in " + str(res) +  " strokes.")
else:
    print("Roberta acknowledges defeat.")

