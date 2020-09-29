class Solution(object):
    def majorityElement(self, nums):
        dic = {}
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1
        for key in dic.keys():
            if (dic[key] > floor(len(nums)/2)):
                return key
        """
        :type nums: List[int]
        :rtype: int
        """
        
