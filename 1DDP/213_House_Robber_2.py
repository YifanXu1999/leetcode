class Solution:
    # Runtime O(n), Space: O(1)
    def rob(self, nums: List[int]) -> int:
        # There are two cases:
        #   1. Do not rob the first house
        #   2. Do not rob the last house

        if (len(nums) == 1):
            return nums[0]
        if (len(nums) == 2):
            return max(nums[0], nums[1])
        # Case 1:
        prev_two = nums[1]
        prev_one = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            tmp = prev_one
            prev_one = max(prev_one, prev_two + nums[i])
            prev_two = tmp

        ans1 = prev_one

        # Case 2
        prev_two = nums[0]
        prev_one = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            tmp = prev_one
            prev_one = max(prev_one, prev_two + nums[i])
            prev_two = tmp
        ans2 = prev_one

        return max(ans2, ans1)
