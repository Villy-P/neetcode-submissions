class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = p1 = 0
        maxRight = p2 = len(height) - 1
        tot = 0
        while p1 <= p2:
            if height[p1] > height[maxLeft]:
                maxLeft = p1
            if height[p2] > height[maxRight]:
                maxRight = p2
            if height[maxLeft] < height[maxRight]:
                tot += height[maxLeft] - height[p1]
                p1 += 1
            else:
                tot += height[maxRight] - height[p2]
                p2 -= 1
        return tot