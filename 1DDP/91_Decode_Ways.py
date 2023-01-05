class Solution:
    # Runtime: O(n), Space: O(n)
    def numDecodings(self, s: str) -> int:
        # dp[i] += dp[i-1] if 1 <= s[i] <= 9
        # dp[i] += dp[i-2] if 1 <= s[i-1: i+1] <= 26
        n = len(s)
        dp = [0 for _ in range(n)]
        val = [int(c) for c in s]
        if (val[0] == 0):
            return 0
        dp[0] = 1
        for i in range(1, n):
            if (val[i] >= 1 and val[i] <= 9):
                dp[i] += dp[i-1]
            if (val[i-1] != 0):
                twoDigit = val[i-1] * 10 + val[i]
            else:
                twoDigit = 0
            if (twoDigit >= 1 and twoDigit <= 26 and twoDigit != 10):
                dp[i] += dp[i-2] if i-2 >= 0 else 1
            if (twoDigit == 10):
                dp[i] += max(dp[i-2], 1)
        return dp[n-1]
