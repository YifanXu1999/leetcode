class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Find the rotation index (actual first index)
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            val = nums[mid]
            leftVal = nums[mid-1] if mid - 1 >= 0 else float('-infinity')
            if (val < leftVal):
                return val
            if (val > nums[high]):
                low = mid + 1
            elif (val == nums[low] and val == nums[high]):
                high -= 1
            elif (nums[high] < nums[low]):
                high = mid - 1
            else:
                high -= 1
        return nums[0]
