class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for idx, i in enumerate(nums):
            start = idx + 1
            end = len(nums) - 1
            while (start < end):
                res = nums[start] + nums[end] + i
                if res == 0:
                    ans.add((i, nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif res > 0:
                    end -= 1
                else:
                    start += 1
        return list(ans)