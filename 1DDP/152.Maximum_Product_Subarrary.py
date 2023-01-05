class Solution:
    # Runtime: O(n) Space: O(n)
    def maxProduct(self, nums: List[int]) -> int:
        # dp_max[i] = max(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
        # dp_min[i] = min(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])

        dp_max = [i for i in nums]
        dp_min = [i for i in nums]
        max_r = nums[0]
        for i in range(1, len(nums)):
            dp_max[i] = max(
                [dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i]])
            dp_min[i] = min(
                [dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i]])
            max_r = max(max_r, dp_max[i])
        return max_r
