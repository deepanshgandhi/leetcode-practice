class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N = len(nums)
        curr_len = N
        for i in range(N-1):
            for j in range(1,curr_len):
                nums[j-1] = (nums[j-1]+nums[j])%10
            curr_len-=1
        return nums[0]