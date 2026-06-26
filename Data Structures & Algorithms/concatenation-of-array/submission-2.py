class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [0] * 2 * len(nums);
        for index, i in enumerate(nums):
            arr[index] = i;
            arr[len(nums) + index] = i;
        return arr;