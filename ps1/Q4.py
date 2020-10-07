from heapq import heappush, heappop
import sys

def solve(a, b, c, h):
    dp = [h] * c
    heap = [0]
    while len(heap) > 0:
        closest = heappop(heap)
        if closest >= h: break
        rem = int(closest % c)
        # no need to update
        if closest >= dp[rem]: continue
        dp[rem] = closest
        heappush(heap, closest  + b)
        heappush(heap, closest  + a)

    res = 0
    first_h = h - h % c
    for i in range(c):
        if dp[i] == h: continue
        curr_last = i + first_h
        if curr_last < h: curr_last += c
        res += (curr_last - dp[i]) // c
    print(int(res))

all_data = """15
4 7 9
"""  

all_data = sys.stdin.read().split('\n')
# all_data = all_data.split('\n')
h = all_data[0]
h = int(h)
next_line = all_data[1]
a, b, c = next_line.split(" ")
a = int(a)
b = int(b)
c = int(c)

solve(a, b, c, h)