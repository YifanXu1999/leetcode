# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while (low <= high):
            mid = (low + high) // 2
            if (not isBadVersion(mid - 1) and isBadVersion(mid)):
                return mid
            if (isBadVersion(mid)):
                high = mid - 1
            else:
                low = mid + 1
        return -1
