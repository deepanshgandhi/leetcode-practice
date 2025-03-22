class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        local_count = 0
        curr = nums[0]
        l= 0
        for r in range(len(nums)):
            if nums[r] == curr:
                local_count+=1
            else:
                local_count = 1
                curr = nums[r]
            if local_count <= 2:
                nums[l] = nums[r]
                l+=1
        return l