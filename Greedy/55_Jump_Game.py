class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        pos = 0
        while (jump != 0 and pos != len(nums) - 1):
            jump -= 1
            pos += 1
            jump = max(jump, nums[pos])
        return pos == len(nums) - 1
