class Solution:
    separator = "ADJHFSDKJHFLKJHSDKJENWMBRJHGJDSF"

    def encode(self, strs: List[str]) -> str:
        ans = []
        for i in strs:
            ans.append(str(len(i)))
            ans.append(":")
            ans.append(str(i))
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        while (len(s) > 0):
            colon = s.index(":")
            num = int(s[0:colon])
            numlen = len(str(num)) + 1
            content = s[(colon + 1):(num + numlen)]
            ans.append(content)
            s = s[(num + numlen):]
        return ans

