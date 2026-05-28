# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def LeftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def RightHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h
        if not root:
            return 0
        
        lh = LeftHeight(root)
        rh = RightHeight(root)

        if lh == rh:
            return (1 << lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)