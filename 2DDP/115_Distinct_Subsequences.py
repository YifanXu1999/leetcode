class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] = dp[i][j-1] if s[i] != t[j]
        # dp[i][j] = dp[i][j-1] + dp[i-1][j-1] if s[i] = t[j]
        row = len(t)
        col = len(s)

        dp = [[0] * (col + 1) for _ in range(0, row+1)]
        dp[0] = [1] * (col + 1)

        for i in range(1, row+1):
            for j in range(1, col+1):
                dp[i][j] = dp[i][j-1]
                if (s[j-1] == t[i-1]):
                    dp[i][j] += dp[i-1][j-1]
        return dp[row][col]
