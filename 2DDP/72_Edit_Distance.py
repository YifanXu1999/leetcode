class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] = dp[i-1][j-1] if word1[i] == word2[j]
        # dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if word[i] != word[j]
        row = len(word1)
        col = len(word2)
        dp = [[0] * (col + 1) for _ in range(row + 1)]

        for i in range(0, row+1):
            for j in range(0, col+1):
                if (i == 0):
                    dp[i][j] = j
                elif (j == 0):
                    dp[i][j] = i
                else:
                    if (word1[i-1] == word2[j-1]):
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1]
                                       [j], dp[i][j-1]) + 1

        return dp[row][col]
