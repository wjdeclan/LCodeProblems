# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepLeaveHelper(self, depth, root):
        if (root is None):
            return None
        if (root.left is None and root.right is None):
            return [depth+1, [root.val]]
        else:
            l = self.deepLeaveHelper(depth+1, root.left)
            r = self.deepLeaveHelper(depth+1, root.right)
            if (r is None or (l is not None and l[0] > r[0])):
                return l
            elif (l is None or r[0] > l[0]):
                return r
            else:
                return [r[0], l[1]+r[1]]
    def deepestLeavesSum(self, root):
        s = 0
        r = self.deepLeaveHelper(0, root)
        for i in r[1]:
            s += i
        return s
        
