class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        while (low <= high):
            mid = (low + high) // 2
            letter = letters[mid]
            prevLetter = letters[mid-1] if mid-1 >= 0 else "1"
            if (prevLetter <= target and letter > target):
                return letter
            if (letter > target):
                high = mid - 1
            else:
                low = mid + 1
        return letters[0]
