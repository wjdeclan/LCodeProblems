class Solution(object):
    def reverseString(self, s):
        t = ""
        for i in range(trunc(len(s)/2)):
            t = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = t
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
