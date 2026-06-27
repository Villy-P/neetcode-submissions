class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            nums[current] = nums[i]
            current += 1
        nums[current] = nums[-1]
        return current + 1