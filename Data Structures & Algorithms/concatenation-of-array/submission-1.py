class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [];
        for index, i in enumerate(nums):
            arr.insert(index, i);
            arr.insert(len(nums) + index, i)
        return arr;