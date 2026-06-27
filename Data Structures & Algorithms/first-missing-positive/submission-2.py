class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        inx = 0
        lowest = 1
        while inx < len(nums):
            i = nums[inx]
            if i == lowest:
                lowest += 1
            if i < 1 or i > len(nums):
                inx += 1
                continue
            if i != inx + 1 and nums[i - 1] != nums[inx]:
                nums[i - 1], nums[inx] = nums[inx], nums[i - 1]
                continue
            inx += 1
        return lowest