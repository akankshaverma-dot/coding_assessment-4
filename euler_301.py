def solve():
    LIMIT_BITS = 30
    dp = [0] * (LIMIT_BITS + 2)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, LIMIT_BITS + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[30]

print(solve())