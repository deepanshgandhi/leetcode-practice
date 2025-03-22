class Solution:
    def jump(self, nums: List[int]) -> int:
        prev_end = -1
        max_jump = 0
        min_jumps = 0
        while max_jump < len(nums)-1:
            curr_max_jump = 0
            for i in range(prev_end+1,max_jump+1):
                curr_max_jump = max(curr_max_jump,i+nums[i])
            max_jump = curr_max_jump
            min_jumps+=1
        return min_jumps