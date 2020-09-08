import sys

def memoize(f):
    memo = {}
    def helper(x, y):
        if (x, y) not in memo:
            memo[(x, y)] = f(x, y)
        return memo[(x, y)]
    return helper

def solve(output):

    def helper(l, r):
        if l == r: return 2
        if l > r: return 0

        min_val = 2 + helper(l + 1, r)
        for i in range(l + 1, r + 1):
            if output[l] == output[i]:
                min_val = min(min_val, helper(i, r) + helper(l + 1, i - 1))
        
        return min_val

    helper = memoize(helper)
    print(len(output) + helper(0, len(output) - 1))

all_data = sys.stdin.read().split('\n')[1:-1]
for idx, row in enumerate(all_data):
    solve(row)
