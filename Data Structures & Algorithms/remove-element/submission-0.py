class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums) - 1, -1, -1):
            if (nums[i] == val):
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
            else:
                k += 1
        return k