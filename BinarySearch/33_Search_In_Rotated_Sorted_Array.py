class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find rotation index
        left = 1
        right = len(nums) - 1
        rotation = 0
        while (left <= right):
            mid = (left + right) // 2
            num = nums[mid]
            leftN = nums[mid - 1]
            if (leftN > num):
                rotation = mid
                break
            if (num > nums[right]):
                left = mid + 1
            else:
                right = mid - 1
        left = 0 + rotation
        right = len(nums) - 1 + rotation
        # Binary search
        while (left <= right):
            mid = (left + right) // 2
            num = nums[mid % len(nums)]
            if (num == target):
                return mid % len(nums)
            if (num < target):
                left = mid + 1
            else:
                right = mid - 1
        return -1
