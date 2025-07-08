class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            word1 = ""
            for ch in word:
                if ch == 'z':
                    word1 += 'a'
                else:
                    word1 += chr(ord(ch) + 1)
            word += word1
        return word[k-1]