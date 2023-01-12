class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr) - 1
        pos = -1
        while (low <= high):
            mid = (low + high) // 2
            val = arr[mid]
            valAfter = arr[mid + 1] if mid + \
                1 < len(arr) else float('infinity')
            if (x >= val and x < valAfter):
                pos = mid
            if (val > x):
                high = mid - 1
            else:
                low = mid + 1
        if (pos == -1):
            pos = 0 if low < len(arr) else len(nums - 1)
        i = pos
        j = pos + 1
        ret = []
        dummy = abs(arr[0]) + abs(arr[len(arr) - 1]) + x
        while (len(ret) < k):
            left = arr[i] if i >= 0 else dummy
            right = arr[j] if j < len(arr) else dummy
            if (abs(x - left) <= abs(x-right)):
                i -= 1
                ret.append(left)
            else:
                j += 1
                ret.append(right)
        ret.sort()
        return ret
