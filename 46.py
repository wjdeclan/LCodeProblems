class Solution(object):
    def permute(self, nums):
        if (len(nums) == 1):
            return [nums]
        elif (len(nums) == 0):
            return []
        ret = []
        for i in range(len(nums)):
            perm = self.permute(nums[0:i]+nums[i+1:])
            for p in perm:
                ret.append([nums[i]]+p)
        return ret
        
