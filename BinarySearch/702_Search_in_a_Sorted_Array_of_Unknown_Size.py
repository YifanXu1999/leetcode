# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if (target < reader.get(0)):
            return -1
        low = 0
        high = target - reader.get(low)
        while (low <= high):
            mid = (low + high) // 2
            if (reader.get(mid) == target):
                return mid
            if (reader.get(mid) == -1 and reader.get(mid + 1) == -1):
                high = mid - 1
            elif (reader.get(mid) > target):
                high = mid - 1
            else:
                low = mid + 1
        return -1
