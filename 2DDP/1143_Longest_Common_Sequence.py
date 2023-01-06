class Solution:
    # Runtime: O(mn) Space: O(mn)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = dp[i-1][j-1] + 1 if s1[i] == s2[j]
        # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        row = len(text1)
        col = len(text2)
        dp = [[0 for _ in range(0, col+1)] for _ in range(0, row+1)]

        for i in range(0, row):
            for j in range(0, col):

                if (text1[i] == text2[j]):
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[row][col]
