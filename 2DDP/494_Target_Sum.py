class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)
        if (target > total):
            return 0
        dp = [[0] * (total * 2 + 1) for _ in range(0, len(nums))]
        dp[0][total - nums[0]] += 1
        dp[0][total + nums[0]] += 1
        for i in range(1, len(nums)):
            for j in range(total * -1, total + 1):
                if (j + nums[i] <= total):
                    dp[i][j + total + nums[i]] += dp[i-1][j+total]
                if (j - nums[i] >= total*-1):
                    dp[i][j + total - nums[i]] += dp[i-1][j+total]

        return dp[len(nums) - 1][target+total]
