class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0
        for i in nums:
            if (i - 1) not in s:
                j = 0
                while j + i in s:
                    j += 1
                if j > m:
                    m = j
        return m