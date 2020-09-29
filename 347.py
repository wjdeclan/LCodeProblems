class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        ret = []
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        sort_dic = sorted(((value, key) for (key, value) in dic.items()), reverse=True)
        for i in range(k):
            ret.append(sort_dic[i][1])
        return ret
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
