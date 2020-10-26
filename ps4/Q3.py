import sys
from collections import defaultdict
text_input = sys.stdin.read().split('\n')

n = int(text_input[0])
parity = [0] + [int(x) & 1 for x in text_input[1].split(" ")]
dp = [0] * (n + 1)


adj = defaultdict(set)
for row in text_input[2:(n + 1)]:
    x, y = map(int, row.split(" "))
    adj[x].add(y)
    adj[y].add(x)

def dfs_a(currNode, currParity):
    dp[currNode] += parity[currNode]
    for nextNode in adj[currNode]:
        if nextNode ^ currParity: 
            ret = dfs_a(nextNode, currNode)
            if parity[nextNode] ^ parity[currNode]: dp[currNode] += ret

    return dp[currNode]

def dfs_b(currNode, currParity):
    if currParity != -1 and parity[currParity] != parity[currNode]:
        dp[currNode] += dp[currParity] - dp[currNode]

    for nextNode in adj[currNode]:
        if nextNode ^ currParity: dfs_b(nextNode, currNode)
    

dfs_a(1, -1)
dfs_b(1, -1)

print(sum(dp[1:]))
