import sys

def memoize(f):
    memo = {}
    def helper(x, y):
        if (x, y) not in memo:            
            memo[(x, y)] = f(x, y)
        return memo[(x, y)]
    return helper

all_data = sys.stdin.read().split('\n')
# all_data = '''7
# 47 12 12 3 9 9 3
# '''
# all_data = all_data.split('\n')

balls = [int(i) for i in all_data[1].split()]
curr_max = 0
prefix = [0] + [sum(balls[:i + 1]) for i in range(len(balls))]

def solve(l, r):

    if l >= r: return True
    
    curr_left = l
    curr_right = r
    while curr_left <= curr_right:
        diff_prefix = prefix[curr_left + 1] - prefix[l] - prefix[r + 1] + prefix[curr_right]
        if diff_prefix < 0:
            curr_left += 1
        elif diff_prefix > 0:
            curr_right -= 1
        elif solve(l, curr_left) and solve(curr_left + 1, curr_right - 1) and solve(curr_right, r):
            return True
        else:
            curr_left += 1

    return False

solve = memoize(solve)

for i in range(len(balls)): 
    for j in range(i, len(balls)): 
        if solve(i, j): 
            curr_max = max(curr_max, prefix[j + 1] - prefix[i])

print(curr_max)
