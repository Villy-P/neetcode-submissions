class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(1, len(nums) - 1):
            start = 0
            end = len(nums) - 1
            while (start < i and end > i):
                res = nums[start] + nums[end] + nums[i]
                if res == 0:
                    ans.add((nums[start], nums[i], nums[end]))
                    start += 1
                    end -= 1
                elif res > 0:
                    end -= 1
                else:
                    start += 1
        return list(ans)