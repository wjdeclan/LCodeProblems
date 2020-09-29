class Solution(object):
    def groupThePeople(self, groupSizes):
        bucket = {}
        ret = []
        for i in range(len(groupSizes)):
            if (groupSizes[i] in bucket):
                bucket[groupSizes[i]].append(i)
            else:
                bucket[groupSizes[i]] = [i]
        for key in bucket.keys():
            i = 0
            while i < len(bucket[key]):
                r = []
                j = 0
                while j < key:
                    r.append(bucket[key][i])
                    j += 1
                    i += 1
                ret.append(r)
        return ret
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        
