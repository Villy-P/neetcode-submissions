class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in t:
            if i not in s:
                return False
            s = s.replace(i, "", 1)
        return len(s) is 0