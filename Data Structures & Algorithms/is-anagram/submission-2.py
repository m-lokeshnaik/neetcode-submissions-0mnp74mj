class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        g={}
        for c in s:
            g[c]=g.get(c,0)+1
        for c in t:
            g[c]=g.get(c,0)-1
        return all(v==0 for v in g.values())


        