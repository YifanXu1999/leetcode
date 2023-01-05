class Solution:
    # Runtime: O(n^2), Space: O(n^2)
    def longestPalindrome(self, s: str) -> str:
        #   dp[i, j]:
        # if i == j => 1
        # if s[i] == s[j] => 2 + dp[i+1, j-1]
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(0, n):
            dp[i][i] = 1
        max_s = s[0]
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                if (s[i] == s[j]):
                    if (j-i == 1):
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 + dp[i+1][j - 1] if dp[i+1][j-1] >= 1 else 0

                    max_s = s[i:j+1] if dp[i][j] > len(max_s) else max_s
        return max_s
