class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for _ in range(len(nums))]
        c = Counter(nums)
        for key, val in c.items():
            arr[val - 1].append(key)
        ans = []
        for i in range(len(arr) - 1, -1, -1):
            if len(arr[i]) > 0:
                for j in arr[i]:
                    ans.append(j)
            if (len(ans) >= k):
                break
        return ans
