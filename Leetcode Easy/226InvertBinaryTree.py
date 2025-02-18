#https://leetcode.com/problems/invert-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if node == None: return
            temp = node.left
            node.left = node.right
            node.right = temp
            helper(node.left)
            helper(node.right)
        helper(root)
        return root