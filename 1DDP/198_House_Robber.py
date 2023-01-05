class Solution:

    # Runtime: O(n), Space: O(1)
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        if (len(nums) == 1):
            return nums[0]
        prev_two = nums[0]
        prev_one = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            tmp = prev_one
            prev_one = max(prev_one, prev_two + nums[i])
            prev_two = tmp
        return prev_one
