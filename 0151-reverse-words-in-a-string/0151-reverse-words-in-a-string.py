class Solution:
    def reverseWords(self, s: str) -> str:
        final = " ".join(s.strip().split()[::-1])
        return final
        