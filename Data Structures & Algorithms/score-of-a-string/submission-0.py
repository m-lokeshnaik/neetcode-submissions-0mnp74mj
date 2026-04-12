class Solution:
    def scoreOfString(self, s: str) -> int:
        n=len(s)
        val=0
        for i in range(1,n):
            val=val+abs(ord(s[i-1])-ord(s[i]))
        return val
