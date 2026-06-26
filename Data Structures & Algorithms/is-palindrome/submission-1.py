class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = re.sub("[^A-Za-z0-9]", "", s).lower()
        for i in range(len(sanitized) // 2):
            if (sanitized[i] != sanitized[-(i+1)]):
                return False
        return True;