def reverse_subarray(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        truek = k % len(nums)
        reverse_subarray(nums, 0, len(nums) - 1)
        reverse_subarray(nums, 0, truek - 1)
        reverse_subarray(nums, truek, len(nums) - 1)