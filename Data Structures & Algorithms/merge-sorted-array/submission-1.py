class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        while i < len(nums1):
            if nums1[i] == 0 and i > m - 1:
                nums1[i] = 1000000001
            for j in range(len(nums2)):
                if nums2[j] < nums1[i]:
                    nums2[j], nums1[i] = nums1[i], nums2[j]
            i += 1