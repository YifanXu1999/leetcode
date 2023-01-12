class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # dp[i][j] = true if
        # 1. dp[i-1][j] = true and s1[i] = s3[i+j]
        # 2. dp[j][i-1] = true and s2[j] = s3[i+j]
        row = len(s1)
        col = len(s2)
        if (row + col != len(s3)):
            return False
        dp = [[False] * (col + 1) for _ in range(0, row + 1)]

        for i in range(0, row+1):
            for j in range(0, col + 1):
                if (i == 0 and j == 0):
                    dp[0][0] = True
                elif (i == 0):
                    dp[0][j] = s2[j-1] == s3[j-1] and dp[0][j-1]
                elif (j == 0):
                    dp[i][0] = s1[i-1] == s3[i-1] and dp[i-1][0]
                elif (dp[i-1][j] and s1[i-1] == s3[i+j-1]):
                    dp[i][j] = True
                elif (dp[i][j-1] and s2[j-1] == s3[i+j-1]):
                    dp[i][j] = True

        return dp[row][col]
