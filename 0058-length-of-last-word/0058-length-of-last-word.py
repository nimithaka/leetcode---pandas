class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = len(s.split()[-1])
        return last_word_length
        