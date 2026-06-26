class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current = []
        zipped = zip(*strs)
        for i in zipped:
            if len(set(i)) != 1:
                break
            current.append(i[0])
        return "".join(current);