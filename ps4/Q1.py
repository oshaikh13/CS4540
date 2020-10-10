import sys

def tile_case(n):
    if n % 2 != 0: return 0
    elif n == 0: return 1
    elif n == 2: return 3
    else: return 2

def num_tilings(n):
    ret_val = tile_case(n * 2)
    for i in range(1, n):
        ret_val += tile_case(i * 2) * num_tilings(n - i)
        ret_val %= 1000000
    return ret_val

def memoize(f):
    memo = {}
    def helper(x):
        if (x) not in memo:            
            memo[(x)] = f(x)
        return memo[(x)]
    return helper

num_tilings = memoize(num_tilings)

input_txt = sys.stdin.read().split('\n')

for i in input_txt[:5]:
    print(num_tilings(int(i) // 2))