class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        small = 0
        big = len(nums) - 1
        while abs(small - big) != 1:
            if nums[small] + nums[big] == target:
                break
            elif nums[small] + nums[big] > target:
                big -= 1
            else:
                small += 1
        return [small + 1, big + 1]