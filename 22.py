class Solution(object):
    def generateParenthesis(self, n):
        if (n == 0):
            return []
        if (n == 1):
            return ["()"]
        ret = []
        for i in range(n):
            outer = self.generateParenthesis(n-i-1)
            inner = self.generateParenthesis(i)
            if (outer == []):
                outer = [""]
            if (inner == []):
                inner = [""]
            for s in outer:
                for t in inner:
                    ret.append("(" + t + ")" + s)
        return ret
