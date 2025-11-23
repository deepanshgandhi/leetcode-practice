class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        for spell in spells:
            low,high = 0,len(potions)-1
            while low<=high:
                mid=(low+high)//2
                if spell*potions[mid]<success:
                    low=mid+1
                else:
                    high=mid-1
            result.append(len(potions) - low)
        return result