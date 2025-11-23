class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeroes = 0
        max_win = 0
        for r in range(len(nums)):
            if nums[r]==0:
                zeroes+=1
                while zeroes>k:
                    if nums[l]==0:
                        zeroes-=1
                    l+=1
            max_win = max(max_win,(r-l+1))
        return max_win