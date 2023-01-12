class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSA = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            if (curr + nums[i] > nums[i]):
                curr = curr + nums[i]
                maxSA = max(curr, maxSA)
            else:
                curr = nums[i]
                maxSA = max(curr, maxSA)
        return maxSA
