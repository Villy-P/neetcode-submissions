import random

class Solution:
    def quicksort(self, nums, start, end):
        if start >= end:
            return
        pivotI = random.randint(start, end)
        pivot = nums[pivotI]
        
        lt = start
        i = start
        gt = end
        
        while i <= gt:
            if nums[i] < pivot:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        
        self.quicksort(nums, start, lt - 1)
        self.quicksort(nums, gt + 1, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums