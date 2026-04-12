class Solution:
    def scoreOfString(self, s: str) -> int:
        n=len(s)
        val=0
        val += sum(abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s)))
        return val
