class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            val = nums[mid]
            leftN = nums[mid-1] if mid-1 >= 0 else float('-inf')
            rightN = nums[mid+1] if mid+1 < len(nums) else float('-inf')
            if (val > leftN and val > rightN):
                return mid
            if (leftN > val and rightN < val):
                high = mid - 1
            elif (leftN < val and rightN > val):
                low = mid + 1
            else:
                low = mid + 1
        return -1
