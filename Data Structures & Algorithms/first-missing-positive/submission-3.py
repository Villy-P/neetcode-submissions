class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        inx = 0
        while inx < len(nums):
            i = nums[inx]
            if i < 1 or i > len(nums):
                inx += 1
                continue
            if i != inx + 1 and nums[i - 1] != nums[inx]:
                nums[i - 1], nums[inx] = nums[inx], nums[i - 1]
                continue
            inx += 1
        for idx, i in enumerate(nums):
            if idx + 1 != i:
                return idx + 1
        return nums[-1] + 1