import sys
sys.setrecursionlimit(10**6) 
n = int(input())
 
adj = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = (int(i) - 1 for i in sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

mod = 10**9 + 7

def dfs(v, p):
  curr_black, curr_white = 1, 1
  for x in adj[v]:
    if x == p: continue
    next_black, next_white = dfs(x, v)
    curr_black = curr_black * next_white % mod
    curr_white = curr_white * (next_black + next_white) % mod
  return curr_black, curr_white
 
curr_black, curr_white = dfs(0, -1)
print((curr_black + curr_white) % mod)