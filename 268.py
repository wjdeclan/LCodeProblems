class Solution(object):
    def missingNumber(self, nums):
        n = range(len(nums)+2)
        for i in nums:
            n.remove(i)
        return n[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        
