import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        ans = []
        while len(nums) != 0:
            ans.append(heapq.heappop(nums))
        return ans