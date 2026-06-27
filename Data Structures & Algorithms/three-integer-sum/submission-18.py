class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for idx, i in enumerate(nums):
            if idx > 0 and nums[idx - 1] == i:
                continue
            start = idx + 1
            end = len(nums) - 1
            while (start < end):
                res = nums[start] + nums[end] + i
                if res == 0:
                    ans.append([i, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < len(nums) and nums[start] == nums[start - 1]:
                        start += 1
                elif res > 0:
                    end -= 1
                else:
                    start += 1
        return ans