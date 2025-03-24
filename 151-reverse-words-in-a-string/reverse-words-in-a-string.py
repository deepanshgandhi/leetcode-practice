class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        words = s.split()
        words.reverse()
        return ' '.join(words)