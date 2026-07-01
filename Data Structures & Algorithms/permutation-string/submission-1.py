class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        left = 0
        right = len(s1)
        while right <= len(s2):
            substr = s2[left:right]
            if Counter(substr) == c:
                return True
            left += 1
            right += 1
        return False