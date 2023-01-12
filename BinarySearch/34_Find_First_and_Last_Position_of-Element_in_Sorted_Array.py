class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        firstIdx = -1
        lastIdx = -1
        while (low <= high):
            mid = (low + high) // 2
            val = nums[mid]
            prevVal = nums[mid - 1] if mid - 1 >= 0 else float('-infinity')
            if (val == target and prevVal < val):
                firstIdx = mid
            if (val < target):
                low = mid + 1
            else:
                high = mid - 1
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            val = nums[mid]
            afterVal = nums[mid + 1] if mid + \
                1 < len(nums) else float('infinity')
            if (val == target and afterVal > val):
                lastIdx = mid
            if (val > target):
                high = mid - 1
            else:
                low = mid + 1
        return [firstIdx, lastIdx]
