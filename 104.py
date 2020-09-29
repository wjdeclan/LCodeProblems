# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def depthCount(self, depth, root):
        if (root is None):
            return 0
        return max([depth, self.depthCount(depth+1, root.left), self.depthCount(depth+1, root.right)])
    def maxDepth(self, root):
        return self.depthCount(1, root)
        """
        :type root: TreeNode
        :rtype: int
        """
        
