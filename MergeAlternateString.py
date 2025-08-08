class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        tempWord = ''
        for i in range(0,min(len1, len2)):
            tempWord = tempWord + word1[i] + word2[i]
        if len1 != len2:
            remWord = word1[len2:len1] if len1 > len2 else word2[len1:len2]
            tempWord = tempWord + remWord
        return tempWord