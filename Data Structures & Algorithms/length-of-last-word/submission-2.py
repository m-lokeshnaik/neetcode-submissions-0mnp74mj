class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=s.split()
        return len(s.split()[-1]) if word else 0