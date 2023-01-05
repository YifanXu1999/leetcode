class Solution:
    

    # Runtime: O(2^n), Memory: O(2^n)
    def climbStairs_1(self, n: int) -> int:
        #  Base Case n = 0, there are 1 way of climbing the stairs
        # Base Case n = 1, there are 1 way of climbing the staris
        # When n >= 2, there are dp(n-1) + dp(n-2) ways of climbing stairs 
        if(n==0):
            return 1
        if(n==1):
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    # Runtime: O(n), Memory: O(1)
    def climbStairs_2(self, n: int) -> int:
        # Base Case: dp[0] = 1, dp[1] = 1
        # When n >= 2: dp[n] = dp[n-1] + dp[n-2]
        if(n < 2):
            return 1
        dp_prev_1 = 1
        dp_prev_2 = 1
        for x in range(2, n+1):
           tmp = dp_prev_2
           dp_prev_2 = dp_prev_1 + dp_prev_2
           dp_prev_1 = tmp
        return dp_prev_2



