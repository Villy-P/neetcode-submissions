import random

class Solution:
    def quicksort(self, nums, start, end):
        if start >= end:
            return
        pivotI = random.randint(start, end)
        nums[end], nums[pivotI] = nums[pivotI], nums[end]
        startLess = start
        for i in range(start, end + 1):
            if nums[i] < nums[end]:
                nums[i], nums[startLess] = nums[startLess], nums[i]
                startLess += 1
        nums[end], nums[startLess] = nums[startLess], nums[end]
        self.quicksort(nums, start, startLess - 1)
        self.quicksort(nums, startLess + 1, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums