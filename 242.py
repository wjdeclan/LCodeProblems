class Solution(object):
    def isAnagram(self, s, t):
        s2 = list(s)
        t2 = list(t)
        try:
            for i in s2:
               t2.remove(i)
        except ValueError:
            return False
        return len(t2) == 0
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
