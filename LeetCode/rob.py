public int rob(int[] num) {
    if(num==null || num.length==0)
        return 0;
 
    int n = num.length;
 
    int[] dp = new int[n+1];
    dp[0]=0;
    dp[1]=num[0];
 
    for (int i=2; i<n+1; i++){
       dp[i] = Math.max(dp[i-1], dp[i-2]+num[i-1]);
    }
 
    return dp[n];
}



def rob(nums):
    if len(nums) == 0:
        return 0

    dp = []
    dp[0] = 0 
    dp[1] = num[0]

    for i in range(2, len(nums)+1): 
        dp[i] = Math.max(dp[i-1], dp[i-2] + num[i-1])

    return dp