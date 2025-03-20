class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        coeff = 1  # Start with C(n-1, 0) = 1
        result = 0

        for i in range(n):
            result = (result + coeff * nums[i]) % 10
            # Update coefficient for the next number
            coeff = coeff * (n - 1 - i) // (i + 1)

        return result