# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if (root == None):
            return float('infinity')
        if (root.left == None and root.right == None):
            return root.val
        if (target > root.val):
            childClosestVal = self.closestValue(root.right, target)
            return root.val if abs(root.val - target) < abs(childClosestVal - target) else childClosestVal
        else:
            childClosestVal = self.closestValue(root.left, target)
            return root.val if abs(root.val - target) < abs(childClosestVal - target) else childClosestVal
