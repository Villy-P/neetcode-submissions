class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        current = ""
        while True:
            if i >= len(strs[0]):
                return current
            eq = strs[0][i]
            for s in strs:
                if i >= len(s) or eq != s[i]:
                    return current
            current += eq
            i += 1