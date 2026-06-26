class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ctrs = Counter(s);
        ctrt = Counter(t)
        return ctrs == ctrt