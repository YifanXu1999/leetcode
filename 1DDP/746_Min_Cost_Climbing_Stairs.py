class Solution:
    # Runtime: O(n), Space: O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        prev_one = 0
        prev_two = 0
        for i in range(2, len(cost)+1):
            tmp = prev_one
            prev_one = min(prev_one + cost[i-1], prev_two + cost[i-2])
            prev_two = tmp
        return prev_one
            