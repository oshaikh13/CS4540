def memoize(f):
    memo = {}
    def helper(x, y):
        if (x, y) not in memo:            
            memo[(x, y)] = f(x, y)
        return memo[(x, y)]
    return helper

def solve(a, game):
    tot = sum(a)
    def helper(l, r):
        if l >= r:
            return 0
    
        if (r - l) % 2 != 0:
            pick_left = a[l] + helper(l + 1, r)
            pick_right = a[r] + helper(l, r - 1)
            return max(pick_left, pick_right)
        else:
            return helper(l + 1, r) if a[l] >= a[r] else helper(l, r - 1)

    helper = memoize(helper)
    diff = 2 * helper(0, len(a) - 1) - tot
    print(f'In game {game}, the greedy strategy might lose by as many as {diff} points.')
    

import sys

class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)

all_data = sys.stdin.read().split('\n')

with recursionlimit(10000):
    for idx, row in enumerate(all_data):
        if row == '0':
            break
        curr_game = [int(x) for x in row.strip().split(" ")][1:]
        solve(curr_game, idx + 1)



