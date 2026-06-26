class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ctrs = Counter(s);
        ctrt = Counter(t)
        for i in ctrs:
            if ctrs[i] != ctrt[i]:
                return False;
        return len(s) == len(t);