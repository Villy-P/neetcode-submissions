class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i1 = 0
        for i in nums:
            if i != val:
                nums[i1] = i
                i1 += 1
        return i1