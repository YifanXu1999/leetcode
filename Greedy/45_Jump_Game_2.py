class Solution:
    def jump(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 0
        count = 1
        start = 0
        end = nums[0]
        while (start <= end and end < len(nums) - 1):
            newEnd = -1
            for i in range(start + 1, end+1):
                newEnd = max(newEnd, i + nums[i])
            start = end
            end = newEnd
            count += 1
        return count
