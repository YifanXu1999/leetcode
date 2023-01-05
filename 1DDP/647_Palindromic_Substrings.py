class Solution:
    # RunTime O(n^2), Space O(n)
    def countSubstrings(self, s: str) -> int:
        #   dp[i, j]:
        # if i == j => 1
        # if s[i] == s[j] => 2 + dp[i+1, j-1]
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count = n
        for i in range(0, n):
            dp[i][i] = 1
        max_s = s[0]
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                if (s[i] == s[j]):
                    if (j-i == 1):
                        dp[i][j] = True
                        count += 1
                    else:
                        if (dp[i+1][j-1]):
                            dp[i][j] = True
                            count += 1

        return count
