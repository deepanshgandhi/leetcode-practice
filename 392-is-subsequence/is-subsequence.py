class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            while j < len(t) and s[i] != t[j]:
                j += 1
            if j == len(t):      # didn't find match
                return False
            i += 1              # found a match
            j += 1              # move both
        return i == len(s)
