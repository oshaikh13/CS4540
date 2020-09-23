import sys
def memoize(f):
    memo = {}
    def helper(x):
        if (x) not in memo:            
            memo[(x)] = f(x)
        return memo[(x)]
    return helper


input_txt = sys.stdin.read().split('\n')
max_group = int(input_txt[0])
rem = input_txt[2:]
names = []
times = []
for idx, elem in enumerate(rem[:(int(input_txt[1]) * 2)]):
    if idx % 2 == 0: names.append(elem)
    else: times.append(int(elem))

groups = []
def solve(l):
    if l >= len(times): return 0
    min_val = float('inf')
    min_name = None
    for i in range(0, max_group):
        curr_min = max(times[l: l + i + 1]) + solve(l + i + 1)
        if curr_min < min_val:
            min_val = curr_min
            min_name = l + i
    groups.append(min_name)
    return min_val

solve = memoize(solve)

print(f"Total Time: {solve(0)}")
groups = groups[::-1]

i = 0
while i < len(times):
    j = i
    while j <= groups[i]:
        print(names[j], end=" ")
        j += 1
    print()
    i = groups[i] + 1

