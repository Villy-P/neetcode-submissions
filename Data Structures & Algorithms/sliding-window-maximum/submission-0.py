import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        left = 0
        right = k
        while right <= len(nums):
            current = nums[left:right]
            heapq.heapify_max(current)
            ans.append(heapq.heappop(current))
            left += 1
            right += 1
        return ans