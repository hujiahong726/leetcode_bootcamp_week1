class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        curr_max = 0
        while left < right:
            temp = (right - left) * min(height[left], height[right])
            if temp > curr_max:
                curr_max = temp
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return curr_max
