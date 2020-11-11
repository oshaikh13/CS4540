N = int(input())
triplets = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0] + x[1], reverse=True)
dp = [0] * (2*10**4 + 1)
for weight, solidness, value in triplets:
    for i in range(weight, weight + solidness): 
        dp[i - weight] = max(dp[i - weight], dp[i] + value)
    dp[solidness] = max(dp[solidness], max(dp[weight + solidness:]) + value)

print(max(dp))
