class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s, e = 0, len(height) - 1
        max_area = min(height[s], height[e]) * (e-s)
        while e > s:
            if height[e] >= height[s]:
                s += 1
            else:
                e -= 1
            max_area = max(max_area, min(height[s], height[e]) * (e-s))
        return max_area