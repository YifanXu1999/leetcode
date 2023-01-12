class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Find the rotation index (actual first index)
        low = 1
        high = len(nums) - 1
        rotation = -1
        while (low <= high):
            mid = (low + high) // 2
            val = nums[mid]
            leftVal = nums[mid-1]
            if (leftVal > val):
                rotation = mid
                return val
            if (val < nums[high]):
                high = mid - 1
            else:
                low = mid + 1
        return nums[0]
