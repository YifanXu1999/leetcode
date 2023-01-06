class Solution:
    # Runtime: O(n) #Space: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][buy]: max(dp[i-1][cooldown] - prcies[i], dp[i-1][buy])
        # dp[i][sell]: dp[i-1][buy] + prices[i]
        # dp[i][cooldown]: max(dp[i-1][cooldown], dp[i-1][sell])

        dp = [[0] * 3 for _ in range(0, len(prices))]

        dp[0][0] = prices[0] * -1
        dp[0][1] = 0
        dp[0][2] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][2]-prices[i], dp[i-1][0])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])

        return max(dp[len(prices)-1])
