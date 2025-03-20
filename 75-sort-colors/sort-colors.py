class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        for r in range(l,len(nums)):
            if nums[r] == 1:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1