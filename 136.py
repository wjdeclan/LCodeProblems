class Solution(object):
    def singleNumber(self, nums):
        seen = []
        for i in nums:
            if i in seen:
                seen.remove(i)
            else:
                seen.append(i)
        return seen[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        
