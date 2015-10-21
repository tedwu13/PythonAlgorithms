def rob(nums):
    if len(nums) == 0:
        return 0

    dp = []
    dp[0] = 0 
    dp[1] = num[0]

    for i in range(2, len(nums)+1): 
        dp[i] = Math.max(dp[i-1], dp[i-2] + num[i-1])

    return dp