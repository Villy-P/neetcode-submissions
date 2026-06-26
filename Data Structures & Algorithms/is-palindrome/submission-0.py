class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = re.sub("[^A-Za-z0-9]", "", s)
        for i in range(len(sanitized) // 2):
            if (sanitized[i].lower() != sanitized[-(i+1)].lower()):
                return False
        return True;