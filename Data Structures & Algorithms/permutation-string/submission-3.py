class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        left = 0
        right = len(s1) - 1
        cwin = Counter(s2[left:right])
        while right < len(s2):
            cwin[s2[right]] += 1
            if cwin == c:
                return True
            cwin[s2[left]] -= 1
            left += 1
            right += 1
        return False