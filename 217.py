class Solution(object):
    def containsDuplicate(self, nums):
        seen = set(nums)
        return len(seen) < len(nums)
        """
        :type nums: List[int]
        :rtype: bool
        """
        
