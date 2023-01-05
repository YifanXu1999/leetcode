class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Base Case: amount = 0 => 0
        # dp[i] = min(for coin in coins: dp[i-coin])
        if (amount == 0):
            return 0
        dp = [-1] * (amount + + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if (i >= coin and dp[i-coin] >= 0):
                    if (dp[i] == -1):
                        dp[i] = dp[i-coin] + 1
                    else:
                        dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount]

        return
