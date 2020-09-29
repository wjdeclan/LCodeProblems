class Solution(object):
    def trap(self, height):
        maxh = 0
        maxes = []
        for i in height:
            if (i > maxh):
                maxh = i
            maxes.append(maxh)
        maxh = 0
        water = 0
        for i in range(len(height)-1, -1, -1):
            if (height[i] > maxh):
                maxh = height[i]
            water = water + min(maxes[i], maxh) - height[i]
        return water
        """
        :type height: List[int]
        :rtype: int
        """
        
