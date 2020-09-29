class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if ((target - nums[i]) in nums and (i != nums.index(target - nums[i]))):
                return [i, nums.index(target - nums[i])]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
