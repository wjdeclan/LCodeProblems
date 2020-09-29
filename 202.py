class Solution(object):
    def isHappy(self, n):
        seen = []
        sn = str(n)
        while (n != 1 and n not in seen):
            seen.append(n)
            sum = 0
            for i in range(len(sn)):
                sum += int(sn[i:i+1])*int(sn[i:i+1])
            n = sum
            sn = str(n)
        return n == 1
        """
        :type n: int
        :rtype: bool
        """
        
