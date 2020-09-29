class Solution(object):
    def productExceptSelf(self, nums):
        rl = []
        out = []
        n = len(nums)
        prod = 1
        for i in range(n-1, -1, -1):
            rl.append(prod)
            prod = prod * nums[i]
        prod = 1
        for i in range(n):
            out.append(prod*rl[n-1-i])
            prod = prod*nums[i]
        return out
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
