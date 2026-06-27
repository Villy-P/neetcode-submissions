class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max = 0
        while left < right:
            l = heights[left]
            r = heights[right]
            area = min(l, r) * (right - left)
            if l > r:
                right -= 1
            else:
                left += 1
            if (area > max):
                max = area
        return max