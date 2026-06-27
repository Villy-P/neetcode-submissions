class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, item in enumerate(nums):
            if (target - item) in map:
                return [map[target - item] + 1, index + 1];
            map[item] = index
        return None