class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        print(sorted(Counter(nums).items()))
        return Counter(nums).most_common(1)[0][0]