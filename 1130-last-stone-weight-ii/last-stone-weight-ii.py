class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target_sum = sum(stones)//2
        memo = {}
        def sum_first_pile(i,target):
            if i<0:
                return 0
            if (i,target) in memo:
                return memo[(i,target)]
            if target >= stones[i]:
                memo[(i,target)] = max((stones[i]+sum_first_pile(i-1,target-stones[i])),sum_first_pile(i-1,target))
            else:
                memo[(i,target)] = sum_first_pile(i-1,target)
            return memo[(i,target)]
        pile_sum = sum_first_pile(len(stones)-1,target_sum)
        second=sum(stones)-pile_sum
        return abs(pile_sum-second)