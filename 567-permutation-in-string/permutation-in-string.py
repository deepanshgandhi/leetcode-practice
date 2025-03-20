class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         s1_hash = [0]*26
         perm_hash = [0]*26
         for char in s1:
            s1_hash[ord(char)-ord('a')]+=1
         l = 0
         for r in range(len(s2)):
             if (r-l+1)>len(s1):
                 perm_hash[ord(s2[l])-ord('a')]-=1
                 l+=1
             perm_hash[ord(s2[r])-ord('a')]+=1
             if s1_hash==perm_hash:
                 return True
         return False