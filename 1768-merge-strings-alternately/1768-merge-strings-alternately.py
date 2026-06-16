class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""
        len_f = len(word1)
        len_s = len(word2)
        limit = max(len_f, len_s)
        for i in range(0, limit):
            if i < len(word1) and i < len(word2):
                final = final + word1[i] + word2[i]
            
            else:
                if len_s > len_f:
                    final = final + word2[i]
                else:
                    final = final + word1[i]
        return final

        