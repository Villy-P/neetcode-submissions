class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for i in strs:
            map[tuple(sorted(Counter(i).items()))].append(i)
        ans = []
        for i in map.values():
            ans.append(i)
        return ans