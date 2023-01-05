class Solution:
    # Runtime O(n), Space: O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = true if there is a word such that dp[i-length(word)] = true and s[i-length(word)+1, i+1] = word
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(0, len(s)):
            for word in wordDict:
                if (i-len(word)+1 >= 0 and s[i-len(word)+1: i+1] == word and dp[i-len(word)+1] == True):
                    dp[i+1] = True
        return dp[len(s)]
